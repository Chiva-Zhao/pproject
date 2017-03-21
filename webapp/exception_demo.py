from flask import Flask, render_template, request, redirect, escape
from vsearch import search4letters
from DBUtils import UseDatabase, ConnectionError, CredentialsError, SQLError

app = Flask(__name__)
app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'zzh',
                          'password': 'zzh',
                          'database': 'pydb', }
app.secret_key = 'YouWillNeverGuess'


# @app.route("/")
# def index() -> '302':
#     return redirect("/entry")

@app.route("/search4_0", methods=['post'])
def do_search0() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    return str(search4letters(phrase, letters))


@app.route("/search4", methods=['post'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    rst = str(search4letters(phrase, letters))
    try:
        log2db_request(request, rst)
    except Exception as exp:
        print('***** Logging failed with this error:', str(exp))
    return render_template('results.html', the_title='查询结果', the_phrase=phrase, the_letters=letters, the_results=rst)


@app.route("/")
@app.route("/entry")
def entry_page() -> 'html':
    return render_template('entry.html', the_title='欢迎来到我的地盘!')


def log_request(req: 'flask_request', res: str) -> None:
    with open('req.log', 'a') as reqlog:
        # print(req.form, file=reqlog, end='|')
        # print(req.remote_addr, file=reqlog, end='|')
        # print(req.user_agent, file=reqlog, end='|')
        # print(req, res, file=reqlog)
        print(req.form, req.remote_user, req.user_agent, res, sep='|', file=reqlog)


def log2db_request(req: 'flask_request', res: str) -> None:
    # raise Exception("Something awful just happened.")
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
        (phrase, letters, ip, browser_string, results)
        values
        (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'], req.form['letters'], req.remote_addr, req.user_agent.browser, res))


@app.route("/viewlog_0")
def view_the_log0() -> str:
    contents = []
    with open('req.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    return str(contents)


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
