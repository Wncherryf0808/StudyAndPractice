"""
自定义过滤器add_template_filter
"""
from flask import Flask, render_template
app = Flask(__name__)

def do_index_class(index):
    if index % 2 == 0:
        return 'line'
    else:
        return ''

app.add_template_filter(do_index_class, 'index_class')

@app.route("/")
def hello():
    goods = [
        {'name': 'python'},
        {'name': 'java'},
        {'name': 'go'},
        {'name': 'C#'}
    ]
    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)