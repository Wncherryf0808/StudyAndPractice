from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    urll = url_for('my_list')
    return "反转地址是：%s" % urll

@app.route('/list/')
def my_list():
    return 'list'


if __name__ == '__main__':
    app.run(debug=True)