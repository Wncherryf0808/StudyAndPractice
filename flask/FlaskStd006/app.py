"""
过滤器
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    student = {
        'name': 'zhangsan',
        'age': -18
    }
    return render_template("index.html", **student)


if __name__ == '__main__':
    app.run(debug=True)