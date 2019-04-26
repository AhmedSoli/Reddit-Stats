import flask as f

app = f.Flask(__name__)

@app.route('/')
def home():
    return f.render_template('home.html')

@app.route('/word_embeddings/<subreddit>')
def word_embeddings(subreddit=None):
    return f.render_template('word_embeddings.html',subreddit=subreddit)
