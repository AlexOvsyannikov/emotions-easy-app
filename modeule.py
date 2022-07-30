import nltk
from LeXmo import LeXmo
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

nltk.download('punkt')


def get_emotions(text):
    emo = LeXmo.LeXmo(text)
    emo.pop('text', None)
    return emo


def sentiment_prediction(text):
    t_b = TextBlob(text)
    _polarity = t_b.sentiment.polarity
    _subjectivity = t_b.sentiment.subjectivity
    _resp = {}
    if _polarity > 0.2:
        _resp['polarity'] = 'positive'
    if -0.1 < _polarity < 0.2:
        _resp['polarity'] = 'neutral'
    else:
        _resp['polarity'] = 'negative'
    _resp['polarity_score'] = _polarity
    _resp['subjectivity_score'] = _subjectivity
    _resp['highlights'] = []

    for token in t_b.sentiment_assessments.assessments:
        _resp['highlights'].append({'word': token[0][0], 'polarity': token[1], 'subjectivity': token[2]})

    return _resp


print(sentiment_prediction('hate you idiot'))
