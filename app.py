import flask as f
from embeddings import nn
import pandas as pd
import io

app = f.Flask(__name__)

@app.route('/')
def home():
	return f.render_template('home.html')

@app.route('/word_embeddings/<subreddit>')
def word_embeddings(subreddit=None):
	return f.render_template('word_embeddings.html',subreddit=subreddit)

@app.route('/word_embeddings/<subreddit>',methods=['POST'])
def nearest_neighbours(subreddit=None):
	str_io = io.StringIO()
	word = f.request.form['word']
	neighbours = nn(word)
	return f.render_template('word_embeddings.html',subreddit=subreddit,word=word,neighbours=neighbours)