import flask as f
from word_embeddings import we_nn

import pandas as pd

app = f.Flask(__name__)

@app.route('/')
def home():
	return f.render_template('home.html')

@app.route('/word_embeddings/<subreddit>')
def word_embeddings(subreddit=None):
	return f.render_template('word_embeddings.html',subreddit=subreddit)

@app.route('/word_embeddings/<subreddit>',methods=['POST'])
def word_embeddings_nn(subreddit=None):
	word = f.request.form['word']
	neighbours = ww_nn(word)
	return f.render_template('word_embeddings.html',subreddit=subreddit,word=word,neighbours=neighbours)

