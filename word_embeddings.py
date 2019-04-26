# Standard library modules.
from itertools import islice

# Third party modules.
from nltk import edit_distance
from gensim.models import FastText as ft

# Local modules

# Globals and constants variables.
MODEL = ft.load_fasttext_format('word_embeddings/Conservative.bin')


def dist(a, b):
    return edit_distance(a, b) / max(len(a), len(b))


def we_nn(word, min_dist=0, topn=100):
    candidates = MODEL.wv.most_similar(positive=[word], topn=topn)
    return list(islice(filter(lambda t: dist(word, t[0]) >= min_dist, candidates), None, topn))

