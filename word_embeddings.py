# Standard library modules.
from itertools import islice
import os

# Third party modules.
from nltk import edit_distance
from gensim.models import FastText as ft

# Local modules

# Globals and constants variables.
models = {}
for subreddit in os.listdir("word_embeddings"):
	if 'bin' in subreddit:
		models[subreddit.replace('.bin','')] =  ft.load_fasttext_format('word_embeddings/' + subreddit)

def dist(a, b):
    return edit_distance(a, b) / max(len(a), len(b))


def we_nn(word,subreddit, min_dist=0, topn=100):
    candidates = models[subreddit].wv.most_similar(positive=[word], topn=topn)
    return list(islice(filter(lambda t: dist(word, t[0]) >= min_dist, candidates), None, topn))

