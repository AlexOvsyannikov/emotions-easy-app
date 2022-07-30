from flask import Flask, request, Response
from modeule import get_emotions, sentiment_prediction

app = Flask(__name__)

UNIVERSAL_KEY = "AlexOffTheBest"


@app.route('/', methods=['GET'])
def main():  # put application's code here
    return 'THIS IS JUST LEARNING PROJECT TO PASS AN IBM PROFESSIONAL CERTIFICATE.\n ' \
           'I FACED A PROBLEM WITH AN IBM ACCOUNT SO I HAVE TO WRITE OWN WEB APIs TO FINISH A COURSE.\n ' \
           '@AlexOFF'


@app.route('/emotion', methods=['GET', "POST"])
def emotion():  # put application's code here
    if request.method == 'GET':
        return get_emotions(text=request.args.get('text', 'NoNe'))
    else:
        if request.form.get('key') == UNIVERSAL_KEY:
            return get_emotions(text=request.form.get('text', 'NoNe'))
        else:
            return Response(status=401, response="USE API KEY")


@app.route('/sentiment', methods=['GET', "POST"])
def sentiment():  # put application's code here
    if request.method == 'GET':
        return sentiment_prediction(text=request.args.get('text', 'NoNe'))
    else:
        if request.form.get('key') == UNIVERSAL_KEY:
            return sentiment_prediction(text=request.form.get('text', 'NoNe'))
        else:
            return Response(status=401, response="USE API KEY")


if __name__ == '__main__':
    app.run()
