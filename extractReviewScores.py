'''Parse a large collection of amazon book reviews and store star ratings for future processing
   Dataset is the 9GB file books_5.json file from http://jmcauley.ucsd.edu/data/amazon/
'''
rec_count=0
ratings=dict()
def process(line):
    '''parse the line as a JSON record, retrieve the bits we want, and store them in the ratings dictionary'''
    import json
    review = json.loads(line)
    score = int(review['overall'])
    asin = review['asin']
    if asin not in ratings:
        thisbook = [0,0,0,0,0,0]
    else:
        thisbook = ratings[asin]

    thisbook[0]+=1 # zero slot is where we count total number of review scores
    thisbook[score]+=1   # count one more of this review score
    ratings[review['asin']]=thisbook

import time
import os
import pickle
t0 = time.time()

dir_path = os.path.dirname(os.path.realpath(__file__))
rev_count=0
with open(dir_path+'./Books_5.json') as f:
    for line in f:
        process(line)
        rev_count+=1
        if rev_count%10000==0:print('+' if rev_count%100000==0 else '.',end='',flush=True)

print("\nProcessed %i reviews for %i books in %.2f seconds"%(rev_count,len(ratings),time.time()-t0))
t1=time.time()

# remove books with too few reviews
too_small = [key for key in ratings if ratings[key][0]<10]
for k in too_small:  del ratings[k]

store=open('./reviews_dict.p',"wb")
pickle.dump(ratings,store)
store.close()
print("Stored %i books with at least 10 ratings in %.2f seconds"%(len(ratings),time.time()-t1))
