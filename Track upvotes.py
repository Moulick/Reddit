import datetime

import praw
import pymongo

# reddit = praw.Reddit(client_id='*',
# client_secret='*',
# user_agent='*',
# username='*',
# password='*')

subbmission_id = '5njti8'

client = pymongo.MongoClient("mongodb://moulick:abc123@localhost")
reddit_db = client.reddit
collection = reddit_db.subbmission_id
print('Database Ok')

# create a reddit instance with site from ./praw.ini
reddit = praw.Reddit('XD')
print('Read only:', reddit.read_only)  # Check if read_only

submission = reddit.submission(id=subbmission_id)
print('ok')
# assume you have a Reddit instance bound to variable `reddit`
print(submission.title)  # to make it non-lazy
# pprint.pprint(vars(submission))

score = submission.score
upvote_ratio = submission.upvote_ratio

ups = score * upvote_ratio
downs = score * (1 - upvote_ratio)
print('score:', score)
print('ratio:', upvote_ratio)
print('ups:', round(ups))
print('downs:', round(downs))

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
