# Standard library modules.
from itertools import islice

# Third party modules.
from nltk import edit_distance
from gensim.models import FastText as ft

# Local modules

# Globals and constants variables.
MODEL = ft.load_fasttext_format('bin/politics.bin')


def dist(a, b):
    return edit_distance(a, b) / max(len(a), len(b))


def nearest_neighbors(word, min_dist=0, topn=10):
    candidates = MODEL.wv.most_similar(positive=[word], topn=10*topn)
    return list(islice(filter(lambda t: dist(word, t[0]) >= min_dist, candidates), None, topn))

