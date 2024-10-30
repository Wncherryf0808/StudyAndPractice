from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/child1')
def child1():
    return render_template('child1.html')


if __name__ == '__main__':
    app.run(debug=True)