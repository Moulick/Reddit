import sys
from datetime import datetime
from time import sleep

import praw
import pymongo

# reddit = praw.Reddit(client_id='*',
# client_secret='*',
# user_agent='*',
# username='*',
# password='*')
if len(sys.argv) == 2:
    url = sys.argv[1]
else:
    url = 'https://redd.it/5p58sx'

client = pymongo.MongoClient("mongodb://moulick:1011sailboat@localhost")
reddit_db = client.reddit
collection = reddit_db[url]
print('Database Ok')

# create a reddit instance with site from ./praw.ini
reddit = praw.Reddit('XD')
print('Read only:', reddit.read_only)  # Check if read_only

print('Ok')
# assume you have a Reddit instance bound to variable `reddit`
print(reddit.submission(url=url).title)  # to make it non-lazy


# submission = reddit.submission(id=submission_id)
# pprint.pprint(vars(submission))


def upvotecount(submission_url):
    submission = reddit.submission(url=submission_url)
    score = submission.score
    upvote_ratio = submission.upvote_ratio

    ups = score * upvote_ratio
    downs = score * (1 - upvote_ratio)
    # print('score:', score)
    # print('ratio:', upvote_ratio)
    # print('ups:', round(ups))
    # print('downs:', round(downs))
    # print(datetime.utcnow())
    post = {'url': submission_url,
            'score': score,
            'ratio': upvote_ratio,
            'ups': round(ups),
            'downs': round(downs),
            "time": datetime.utcnow()}

    _ = collection.insert_one(post).inserted_id


count = 1

while True:
    try:
        print('trying')
        upvotecount(url)
        print(count, ':', 'another one')
        count += 1
        sleep(5)
    except Exception as e:
        continue
        print(e)
        continue
