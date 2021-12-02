"""
    before running the app from terminal, execute following code:

export FLASK_APP=my_app
flask run

    for running a public server, execute
flask run --host=0.0.0.0
"""
from flask import Flask
from flask import request
from flask.helpers import url_for
from flask.templating import render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def homepage():
    return 'This is the starting page.'

@app.route('/hello')
def hello():
    return "<p>Hello World!</p>"

@app.route('/<input>')
def reply(input):
    return f'You said:\n{escape(input)}'

@app.route('/<path:input>')
def default(input):
    return f'unknown path:\n{escape(input)}'

@app.route('/repeat/<input>/<int:number>')
def repeat(input, number: int):
    res_ = "<pre>You said:\n"
    for i in range(number):
        res_ += f"{escape(input)}\n"
    return res_ + "</pre>"

@app.route("/template/")
@app.route('/template/<input>', methods=['POST', 'GET'])
def my_template(input=None):
    if request.method == 'POST':
        res_ = "<pre>You POSTed:\n"
        for key_ in request.form:
            res_ += f"{escape(request.args.get(key_))}\n"
            return res_ + "</pre>"
    return render_template("my_template.html", input=input)


MY_PORT = 4449
if __name__ == "__main__":
    app.run('localhost', MY_PORT)
    with app.test_request_context():
        example_img_url = url_for("static", filename="example.jpg")
        print(example_img_url)
    with app.test_request_context("/template?hello=world", method="POST") as _post:
        _post.pop()
