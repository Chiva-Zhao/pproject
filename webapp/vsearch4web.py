from flask import Flask, render_template, request, redirect, escape
from vsearch import search4letters

app = Flask(__name__)


# @app.route("/")
# def index() -> '302':
#     return redirect("/entry")


@app.route("/search4_1", methods=['post'])
def do_search1() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    return str(search4letters(phrase, letters))


@app.route("/search4", methods=['post'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    rst = str(search4letters(phrase, letters))
    log_request(request, rst)
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
        print(req.form, req.remote_user, req.user_agent, file=reqlog, end='|')


@app.route("/viewlog")
def view_the_log() -> str:
    with open('req.log') as log:
        contents = escape(log.read())
    return contents


if (__name__ == '__main__'):
    app.run(debug=True)
