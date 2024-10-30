"""
set和with
set在模板定义变量后，就可以在之后使用，类 全局变量
with在模板定义后，只能在代码块内使用， 类 局部变量

<body>
    {% set username='zzz' %}
    <p>{{ username }}</p>
</body>

<body>
    {% with username = 'zzz' %}
    <p>{{ username }}</p>
    {% endwith %}
</body>

{% with %}
    {% set username='zzz' %}
    <p>{{ username }}</p>
{% endwith %}
"""
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

