from flask import Flask, request 
app = Flask(__name__)
@app.route('/')
def home():
         return "welcome to flask!"
@app.route('/hello/<name>')
def hello(name):
         return f"hello, {name}!"
if __name__ =='__main_':
        app.run(debug=True)