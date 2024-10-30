from flask import Flask, request, render_template

html_txt = """
<!DOCTYPE html>
<html>
    <body>
        <h2>如果收到了GET请求</h2>
        <form method='post>
        <input type='submit' value="按下我发送post请求">
        </form>
    </body>
</html>
"""

app = Flask(__name__)
@app.route('/aaa', method=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        return "get请求"
    return "post请求"


if __name__ == '__main__':
    app.run(debug=True)
