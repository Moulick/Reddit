from datetime import datetime
from time import sleep

import praw
import pymongo


# reddit = praw.Reddit(client_id='*',
# client_secret='*',
# user_agent='*',
# username='*',
# password='*')

# if len(argv) == 2:
#     url = argv[1]
# else:
#     url = 'https://redd.it/5p58sx'

# takes a reddit submission instance and adds the upvote score etc to the mongo db
def upvotecount(submission):
    # submission = reddit.submission(url=submission_url)
    score = submission.score
    upvote_ratio = submission.upvote_ratio

    ups = score * upvote_ratio
    downs = score * (1 - upvote_ratio)
    # print('score:', score)
    # print('ratio:', upvote_ratio)
    # print('ups:', round(ups))
    # print('downs:', round(downs))
    # print(datetime.utcnow())
    url = 'https://redd.it/' + submission.id
    post = {'url': url,
            'title': submission.title,
            'created': submission.created_utc,
            'score': score,
            'ratio': upvote_ratio,
            'ups': round(ups),
            'downs': round(downs),
            "time": datetime.utcnow()}
    collection = reddit_db[url]
    _ = collection.insert_one(post).inserted_id


client = pymongo.MongoClient("mongodb://moulick:1011sailboat@localhost")
reddit_db = client.reddit
# collection = reddit_db[url]
print('Database Ok')

reddit = praw.Reddit('XDD')  # create a reddit instance with site from ./praw.ini
subreddit = reddit.subreddit('funny')
print('Read only:', reddit.read_only)  # Check if read_only

print('Ok')

# print(reddit.submission(url=url).title)  # to make it non-lazy

# pprint.pprint(vars(submission))


count = 1

running = True
while running:
    try:
        for submission in subreddit.rising(limit=25):
            if submission.score > 20:
                post = {'url': 'https://redd.it/' + submission.id,
                        'title': submission.title,
                        'id': submission.id,
                        'created_utc': submission.created_utc
                        }
                tracked = reddit_db['tracked']
                _ = tracked.insert_one(post).inserted_id
            limits = reddit.auth.limits
            print(limits)
            if limits['remaining'] < 10:
                print('Limit remaining below 10')
                sleep(60)  # sleep to get recharge api request limit
            else:
                sleep(5)  # current value:5, change to 900 later
    except KeyboardInterrupt:
        print('Termination received. Goodbye!')
        running = False
    except Exception as e:
        print(e)
        continue
