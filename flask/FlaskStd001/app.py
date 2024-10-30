# import config
from flask import Flask


app = Flask(__name__)

# 通过字符串形式加载文件
# app.config.from_file
# app.config.from_json
# app.config.from_object(config)

# print(app.config["TOKEN_KEY"])

@app.route("/blog/list/<any(python, flask, django):category>")
def blog_detail(category):
    return "<h1>您查找的博客分类为: %s<h1>" % category


if __name__ == '__main__':
    app.run(debug=True)