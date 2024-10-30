"""
页面跳转和重定向
"""

from flask import Flask, url_for,redirect

app = Flask(__name__)

@app.route("/")
def index():
    print("首先访问了这个视图")
    urll = url_for('user_login')
    return redirect(urll)

@app.route("/user_login")
def user_login():
    return "需要先登录才能访问首页"


if __name__ == '__main__':
    app.run(debug=True)