from datetime import datetime
from time import sleep

import praw
import pymongo

# reddit = praw.Reddit(client_id='*',
# client_secret='*',
# user_agent='*',
# username='*',
# password='*')

subbmission_id = '5nnd1r'

client = pymongo.MongoClient("mongodb://moulick:abc123@localhost")
reddit_db = client.reddit
collection = reddit_db.music
print('Database Ok')

# create a reddit instance with site from ./praw.ini
reddit = praw.Reddit('XD')
print('Read only:', reddit.read_only)  # Check if read_only

submission = reddit.submission(id=subbmission_id)
print('ok')
# assume you have a Reddit instance bound to variable `reddit`
print(submission.title)  # to make it non-lazy
# pprint.pprint(vars(submission))


def upvotecount(submission):
    score = submission.score
    upvote_ratio = submission.upvote_ratio

    ups = score * upvote_ratio
    downs = score * (1 - upvote_ratio)
    # print('score:', score)
    # print('ratio:', upvote_ratio)
    # print('ups:', round(ups))
    # print('downs:', round(downs))
    # print(datetime.utcnow())
    post = {'score': score,
            'ratio': upvote_ratio,
            'ups': round(ups),
            'downs': round(downs),
            "time": datetime.utcnow()}

    post_id = collection.insert_one(post).inserted_id


count = 1
while True:
    upvotecount(submission)
    print(count, ':', 'another one')
    count += 1
    sleep(5)
