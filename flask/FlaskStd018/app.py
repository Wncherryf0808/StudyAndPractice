from flask import Flask, render_template, views, request

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html')

class LoginView(views.MethodView):
    def get(self):
        return render_template("index.html")

    def post(self):
        username = request.form.get("username")
        password = request.form.get('pwd')

        if username == 'admin' and password == 'admin':
            return "用户名正确，可以登录"
        else:
            return "用户名不正确，不能登录"

app.add_url_rule(rule='/login', view_func=LoginView.as_view('loginview'))

if __name__ == "__main__":
    app.run(debug=True)