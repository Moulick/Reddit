import pprint

import praw
import pymongo

# reddit = praw.Reddit(client_id='*',
# client_secret='*',
# user_agent='*',
# username='*',
# password='*')

submission_id = '5oidvk'

client = pymongo.MongoClient("mongodb://moulick:1011sailboat@localhost")
reddit_db = client.reddit
collection = reddit_db.shkreli
print('Database Ok')

# create a reddit instance with site from ./praw.ini
reddit = praw.Reddit('XD')
print('Read only:', reddit.read_only)  # Check if read_only

print('Ok')
# assume you have a Reddit instance bound to variable `reddit`
submission = reddit.submission(id=submission_id)
print(submission.title)  # to make it non-lazy

pprint.pprint(vars(submission))
