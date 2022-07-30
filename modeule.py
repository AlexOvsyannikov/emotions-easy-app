import nltk
from LeXmo import LeXmo
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

nltk.download('punkt')


def get_emotions(text):
    emo = LeXmo.LeXmo(text)
    emo.pop('text', None)
    return emo


def sentiment_prediction(x):
    _sc = TextBlob(x).sentiment.polarity
    if _sc > 0.2:
        return {'sentiment': 'positive'}
    if -0.1 < _sc < 0.2:
        return {'sentiment': 'neutral'}
    else:
        return {'sentiment': 'negative'}


