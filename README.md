# reviewDistributions
Discover some interesting things about Amazon book reviews....

Uses a large (9GB) dataset of reviews from http://jmcauley.ucsd.edu/data/amazon/ .  Processes them to retrieve the 1- to 5-star ratings for each book in the dataset.  Puts that into a dictionary, and writes it to a file.  This can take a few minutes!

Then we can read that dictionary and process it to look for ways to find interesting books other than just the 5-star reviews.  One such algorithm that it tests is  ((# 1-star reviews) + (# 5-star reviews)) / (# 3-star reviews) which is designed to look for books people either love or hate.  

Average star ratings across all the books in the set with at least ten reviews:
Average 1-star percent:  3.6%
Average 2-star percent:  4.7%
Average 3-star percent: 10.8%
Average 4-star percent: 25.2%
Average 5-star percent: 55.7%
