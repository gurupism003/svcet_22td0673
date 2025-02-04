from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, this is the home page'

@app.route('/welcome/<name>')
def welcome(name):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
