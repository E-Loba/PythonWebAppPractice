from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/hello')
def hello():
    return "Hello World"


MY_PORT = 4449
if __name__ == "__main__":
    app.run('localhost', MY_PORT)
