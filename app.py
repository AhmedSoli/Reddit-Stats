import flask as f
from embeddings import nn
import pandas as pd
import io

app = f.Flask(__name__)
str_io = io.StringIO()


@app.route('/')
def home():
	return f.render_template('home.html')

@app.route('/word_embeddings/<subreddit>')
def word_embeddings(subreddit=None):
	return f.render_template('word_embeddings.html',subreddit=subreddit)

@app.route('/word_embeddings/<subreddit>',methods=['POST'])
def nearest_neighbours(subreddit=None):
	word = f.request.form['word']
	neighbours = nn(word)
	neighbours = pd.DataFrame.from_dict(neighbours).to_html(buf=str_io, classes='table table-striped')
	return f.render_template('word_embeddings.html',subreddit=subreddit,word=word,neighbours=str_io.getvalue())