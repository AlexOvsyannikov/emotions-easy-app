from flask import Flask, request
from modeule import get_emotions
app = Flask(__name__)


@app.route('/', methods=['GET', "POST"])
def hello_world():  # put application's code here
    if request.method == 'GET':
        return get_emotions(text=request.args.get('text', 'NoNe'))
    else:
        return get_emotions(text=request.form.get('text', 'NoNe'))


if __name__ == '__main__':
    app.run()
