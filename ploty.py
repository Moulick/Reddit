import datetime

import matplotlib.pyplot as plt
import praw
import pymongo

client = pymongo.MongoClient("mongodb://moulick:1011sailboat@localhost")
reddit_db = client.reddit

submission_url = 'https://redd.it/5qbkqm'
collection = reddit_db[submission_url]
# Check if time is in increasing order to verify time data
# if sorted(time_in_sec) == time_in_sec:
#     print('ok')
# else:
#     print('not ok')
print(submission_url)


def created_time(submission_url):
    reddit = praw.Reddit('XD')
    submission = reddit.submission(url=submission_url)
    print(submission.title)
    # print(int(submission.created_utc))
    return int(submission.created_utc)


def i_plot(created_utc):

    fields = {'ups': True,
              'time': True,
              '_id': False}
    ups_list = []
    time_list_utc = []
    time_in_sec = []
    projects = collection.find(projection=fields)
    for project in projects:
        ups_list.append(project['ups'])  # Append upsvotes
        time_list_utc.append(project['time'])  # Append
        time_in_sec.append((project['time'] - datetime.datetime(1970, 1, 1)).total_seconds() - created_utc)
    # print('ups_list', ups_list)
    # print('time_list_utc', time_list_utc)
    #
    # print('time_in_sec', time_in_sec)

    return time_in_sec, ups_list


created = created_time(submission_url)

f, ax = plt.subplots(1)

time, ups = i_plot(created)
ax.plot(time, ups, markersize=0.1)
plt.ylabel('No of Upvotes')
plt.xlabel('Time in sec from post creation')
ax.set_title(submission_url)
ax.set_ylim(ymin=0)
ax.set_xlim(xmin=0)
plt.show()
