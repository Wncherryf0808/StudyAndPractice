import subprocess

from flask import Flask, render_template

app = Flask(__name__)

list_info = ["组别","类型","项目名","属性","版本类型", "版本", "负责人", "优先级", "状态", "预估人力", "实际人力"]

@app.route("/")
def get_device_info():
    process = subprocess.Popen(['adb', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    info = stdout.decode().strip().split()[-2]

    info_text = "信息内容："
    return render_template('index.html', info_text=info_text, info= info)



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")