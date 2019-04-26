import pickle
import gzip
from sklearn.metrics.pairwise import cosine_similarity



vectors = pickle.load(gzip.open('subreddit_embeddings/0to500.pickle.gz',"rb"))

def se_nn(board,k=100,skip=[]):
	similarity = {}

	if len(skip) == 0:
	    skip = [board]

	for subreddit in vectors:
	    if subreddit not in skip:
	        similarity[subreddit] = cosine_similarity( \
	            vectors[board].reshape(1,-1),vectors[subreddit].reshape(1,-1))

	return sorted(similarity.items(),key = lambda x:x[1],reverse=True)[0:k]