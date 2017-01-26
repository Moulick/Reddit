from datetime import datetime

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

reddit = praw.Reddit('XD')  # create a reddit instance with site from ./praw.ini
subreddit = reddit.subreddit('Funny')
print('Read only:', reddit.read_only)  # Check if read_only

print('Ok')

# print(reddit.submission(url=url).title)  # to make it non-lazy

# pprint.pprint(vars(submission))


count = 1

running = True
while running:
    try:
        for submission in subreddit.rising(limit=10):
            print('title:', submission.title)
            print('score:', submission.score)  # Output: the submission's score
            upvotecount(submission)
            print('https://redd.it/' + submission.id, sep='')
            print(submission.url)  # Output: The URL
            print(reddit.auth.limits)
            # sleep(5)
    except KeyboardInterrupt:
        print('Termination received. Goodbye!')
        running = False
    except Exception as e:
        print(e)

        # try:
        #     print(count, ':', 'trying')
        #     upvotecount(url)
        #     print(count, ':', 'another one')
        #     count += 1
        #     sleep(5)
        # except Exception as e:
        #     continue
        #     print(e)
        #     continue
