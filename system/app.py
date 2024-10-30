from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

name_list = ["组别","类型", "项目名","属性", "版本类型"]
# 显示登录表单
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        if username == 'admin' and password == 'admin':
            return redirect(url_for("info"))
        else:
            return render_template('index.html')
    return render_template("index.html")

# 处理登录请求
@app.route("/info")
def info():
    return render_template('info.html', name_list=name_list)



if __name__== "__main__":
    app.run(debug=True)