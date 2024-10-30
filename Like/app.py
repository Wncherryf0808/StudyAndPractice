from flask import Flask, render_template, request

app = Flask(__name__)

data = [
    {"id": 1, "name": "zhangsan", "score": "A", "remark": "优秀", "num": 0},
    {"id": 2, "name": "lisi", "score": "B", "remark": "良好", "num": 0},
    {"id": 3, "name": "wangwu", "score": "C", "remark": "及格", "num": 0},
    {"id": 4, "name": "zhaoliu", "score": "D", "remark": "不及格", "num": 0}
]

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/dianzan')
def dianzan():
    id = request.args.get("id")
    data[(int(id)-1)]['num'] += 1
    return  render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)