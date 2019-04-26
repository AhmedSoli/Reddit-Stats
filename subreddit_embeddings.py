import pickle
import gzip
from sklearn.metrics.pairwise import cosine_similarity

vectors = pickle.load(gzip.open('subreddit_embeddings/0to50k.pickle.gz',"rb"))
boards_sorted = pickle.load(gzip.open('subreddit_embeddings/subreddits_sorted_active_members.pickle.gz',"rb"))

def so_nn(board):
    if board not in boards_sorted:
        return [('subreddit does not exist',0)]
    results = []
    idx = (-vectors[board]).argsort()
    i = 0
    for id in idx:
        name = boards_sorted[id + 1]
        #if name in members and len(members[name]['users']) > filter:
        i += 1
        results.append(name)
        if i == 100:
            break
    return results

def se_nn(board,k=100,skip=[]):
    if board not in boards_sorted:
        return [('subreddit does not exist',0)]
	similarity = {}

	if len(skip) == 0:
	    skip = [board]

	for subreddit in vectors:
	    if subreddit not in skip:
	        similarity[subreddit] = cosine_similarity( \
	            vectors[board].reshape(1,-1),vectors[subreddit].reshape(1,-1))

	return sorted(similarity.items(),key = lambda x:x[1],reverse=True)[0:k]