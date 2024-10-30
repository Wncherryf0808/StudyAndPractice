"""
页面重定向
"""

from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/login')
def login():
    return 'login page'

@app.route('/profile')
def profile():
    name = request.args.get('name')
    if not name:
        # flask.redirect(location, code=302)
        # URL:重定向到哪个URL， code：状态码， 默认302， 暂时性重定向
        # 301 永久性重定向
        return redirect('/login')
    else:
        return name


if __name__ == '__main__':
    app.run(debug=True)