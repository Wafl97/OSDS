from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def default():
    return 'Hello world!'

@app.route("/welcome")
def welcome():
    name = request.args[0]
    return 'welcome' + name

if __name__ == '__main__':
    app.run(host='0.0.0.0')