from flask import Flask, render_template
from ..backend.main import *

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    print('hello')
    data = main()
    print(data)
    return "<p>here</p>"

@app.route("/about")
def about():
    return "<h1>About Page</h1>"

if __name__ == '__main__':
    app.run(debug=True)