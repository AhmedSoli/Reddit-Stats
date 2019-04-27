import flask as f
import os
from word_embeddings import we_nn
from subreddit_embeddings import se_nn
from subreddit_embeddings import so_nn


import pandas as pd

app = f.Flask(__name__)

@app.route('/')
def home():
	return f.render_template('home.html')

@app.route('/word_embeddings/<subreddit>')
def word_embeddings(subreddit=None):
	return f.render_template('word_embeddings.html',subreddit=subreddit)

@app.route('/word_embeddings/<subreddit>',methods=['POST'])
def nearest_neighbours(subreddit=None):
	word = f.request.form['word']
	neighbours = we_nn(word)
	return f.render_template('word_embeddings.html',subreddit=subreddit,word=word,neighbours=neighbours)

@app.route('/subreddit_embeddings')
def subreddit_embeddings():
	return f.render_template('subreddit_embeddings.html')

@app.route('/subreddit_embeddings',methods=['POST'])
def subreddit_embeddings_nn():
	subreddit = f.request.form['subreddit']
	neighbours = se_nn(subreddit)
	return f.render_template('subreddit_embeddings.html',subreddit=subreddit,neighbours=neighbours)

@app.route('/subreddit_overlap')
def subreddit_overlap():
	return f.render_template('subreddit_overlap.html')

@app.route('/subreddit_overlap',methods=['POST'])
def subreddit_overlap_nn():
	subreddit = f.request.form['subreddit']
	neighbours = so_nn(subreddit)
	return f.render_template('subreddit_overlap.html',subreddit=subreddit,neighbours=neighbours)

@app.route('/word_clouds/<subreddit>')
def word_clouds(subreddit=None):
	images = []
	for file in os.listdir("static/word_clouds"):
		if file.split('-')[0] == subreddit:
			images.append(file)
	return f.render_template('word_clouds.html',subreddit=subreddit,images=images)
