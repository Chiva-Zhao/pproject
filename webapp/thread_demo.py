from flask import Flask, render_template, request, escape, copy_current_request_context
from vsearch import search4letters
from DBUtils import UseDatabase, ConnectionError, CredentialsError, SQLError
from threading import Thread
from time import sleep

app = Flask(__name__)
app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'zzh',
                          'password': 'zzh',
                          'database': 'pydb', }
app.secret_key = 'YouWillNeverGuess'


@app.route("/search4", methods=['post'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    rst = str(search4letters(phrase, letters))

    @copy_current_request_context
    def log_request(req: 'flask_request', res: str) -> None:
        sleep(5)  # This makes log_request really slow...
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """insert into log
            (phrase, letters, ip, browser_string, results)
            values
            (%s, %s, %s, %s, %s)"""
            cursor.execute(_SQL,
                           (req.form['phrase'], req.form['letters'], req.remote_addr, req.user_agent.browser, res))

    try:
        t = Thread(target=log_request, args=(request, rst))
        t.start()
    except Exception as exp:
        print('***** Logging failed with this error:', str(exp))
    return render_template('results.html', the_title='查询结果', the_phrase=phrase, the_letters=letters, the_results=rst)


@app.route("/")
@app.route("/entry")
def entry_page() -> 'html':
    return render_template('entry.html', the_title='欢迎来到我的地盘!')


@app.route("/viewlog")
def view_the_log() -> 'html':
    _SQL = """select phrase, letters,ip,browser_string,results from log"""
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            cursor.execute(_SQL)
            contents = cursor.fetchall()
        return render_template('viewlog.html', the_title='查看日志',
                               the_row_titles=['短语', '表单数据', 'IP', '客户端', '结果'],
                               the_data=contents)
    except ConnectionError as err:
        print('Is your database switched on? Error:', str(err))
    except CredentialsError as err:
        print('User-id/Password issues. Error:', str(err))
    except SQLError as err:
        print('Is your query correct? Error:', str(err))
    except Exception as err:
        print('Something went wrong:', str(err))
    return 'Error'


if (__name__ == '__main__'):
    app.run(debug=True)
