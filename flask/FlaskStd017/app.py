from flask import Flask, views, typing as ft, render_template

app = Flask(__name__)

class Ads(views.View):
    def __init__(self):
        super().__init__()
        self.context = {'ads': '这是对联广告'}

class Index(Ads):
    def dispatch_request(self):
        return render_template('index.html', **self.context)


class Login(Ads):
    def dispatch_request(self) -> ft.ResponseReturnValue:
        return render_template('login.html', **self.context)

class Register(Ads):
    def dispatch_request(self) -> ft.ResponseReturnValue:
        return render_template('register.html', **self.context)


app.add_url_rule(rule='/', endpoint='index', view_func=Index.as_view('Index'))
app.add_url_rule(rule='/login/', endpoint='login', view_func=Login.as_view('Login'))
app.add_url_rule(rule='/register/', endpoint='register', view_func=Register.as_view('Register'))

if __name__ == '__main__':
    app.run(debug=True)