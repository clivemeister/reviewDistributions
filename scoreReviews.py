
'''Read a previously-produced dictionary of book review star ratings, and score with madhack algorithm'''
import time
import os
import pickle

def madhack12_score(book):
    return (book[1]+book[5])/book[3]

t0 = time.time()
ratings=dict()  # dictionary, keyed by book "asin" number, with value a 6-part tuple, (num_scores, 1starcount, ... ,5starcount)
dir_path = os.path.dirname(os.path.realpath(__file__))
store=open(dir_path+'./reviews_dict.p',"rb")
ratings=pickle.load(store)
store.close()
print("Retrieved %i books with at least 10 ratings in %.2f seconds"%(len(ratings),time.time()-t0))

# summarise overall results
tot_scores=[0]*6
for i in range(6):
    tot_scores[i]=sum([ratings[key][i] for key in ratings])
    if i>=1:
        print("Average %i-star percent: %4.1f%%"%(i,100*tot_scores[i]/tot_scores[0]))

# run the comparison: each book is keyed by Amazon's "asin"
madhack_scores = [madhack12_score(ratings[key]) for key in ratings if ratings[key][3]>0]

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
plt.hist(madhack_scores,bins=range(0,20))
print("\n",stats.describe(madhack_scores))

t=0
for k,v in ratings.items():
    if v[3]>0 and madhack12_score(v)>20:
        print("https://www.amazon.com/s?k=%s score=%4.1f, star count=%s"%(k,madhack12_score(v),v[1:6]))
        t+=1
        if t>20:break   #stop after first few or we'd be here forever
