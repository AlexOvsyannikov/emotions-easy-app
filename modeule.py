import nltk
from LeXmo import LeXmo

nltk.download('punkt')


def get_emotions(text):
    emo = LeXmo.LeXmo(text)
    emo.pop('text', None)
    return emo
