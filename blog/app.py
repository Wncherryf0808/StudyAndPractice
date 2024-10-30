from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# 多视图绑定
@app.route("/hi")
@app.route("/hello")
def say_hello():
    return "<h1>Hello World!</h1>"

# 动态视频绑定
@app.route("/greet", defaults={'name': 'Programmer'})
@app.route("/greet/<name>")
def greet(name):
    return '<h1>Hello, %s!</h1>' % name

# @app.route("/greet")
# @app.route("/greet/<name>")
# def greet(name='Programmer'):
#     return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':
    app.run(debug=True)