from flask import Flask, session
from checker import check_logged_in

app = Flask(__name__)
app.secret_key = 'YouWillNeverGuess'


@app.route("/login")
def dologin() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out.'


@app.route('/status')
def check_status() -> str:
    if 'logged_in' in session:
        return "登录状态"
    return "登出状态"


# def check_logged_in() -> bool:
#     if 'logged_in' in session:
#         return True
#     return False


@app.route('/page1')
@check_logged_in
def page1() -> str:
    return 'This is page 1.'


@app.route('/page2')
@check_logged_in
def page2() -> str:
    return 'This is page 2.'


if __name__ == "__main__":
    app.run(debug=True)
