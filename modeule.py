import nltk
from LeXmo import LeXmo
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
import requests
from bs4 import BeautifulSoup
nltk.download('punkt')

u_a = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us; Silk/1.1.0-80) AppleWebKit/533.16 (KHTML, like Gecko) ' \
      'Version/5.0 Safari/533.16 Silk-Accelerated=true '


def get_emotions(text):
    if text.startswith('http'):
        text = BeautifulSoup(requests.get(text, headers={'User-Agent': u_a}).text, features="html.parser").get_text()
    emo = LeXmo.LeXmo(text)
    emo.pop('text', None)
    return emo


def sentiment_prediction(text):
    if text.startswith('http'):
        text = BeautifulSoup(requests.get(text, headers={'User-Agent': u_a}).text, features="html.parser").get_text()
    t_b = TextBlob(text)
    _polarity = t_b.sentiment.polarity
    _subjectivity = t_b.sentiment.subjectivity
    _resp = {}
    if _polarity > 0.2:
        _resp['polarity'] = 'positive'
    elif -0.1 < _polarity < 0.2:
        _resp['polarity'] = 'neutral'
    else:
        _resp['polarity'] = 'negative'
    _resp['polarity_score'] = _polarity
    _resp['subjectivity_score'] = _subjectivity
    _resp['highlights'] = []

    for token in t_b.sentiment_assessments.assessments:
        _resp['highlights'].append({'word': token[0][0], 'polarity': token[1], 'subjectivity': token[2]})

    return _resp


# print(sentiment_prediction('you are the best man on earth'))
