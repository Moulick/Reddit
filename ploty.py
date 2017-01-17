import datetime

import matplotlib.pyplot as plt
import pymongo

client = pymongo.MongoClient("mongodb://moulick:1011sailboat@localhost")
reddit_db = client.reddit
collection = reddit_db.shkreli
print('Database Ok')


# Check if time is in increasing order to verify time data
# if sorted(time_in_sec) == time_in_sec:
#     print('ok')
# else:
#     print('not ok')


def i_plot():
    created = 1484663909
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
        time_in_sec.append((project['time'] - datetime.datetime(1970, 1, 1)).total_seconds() - created)
    # print('ups_list', ups_list)
    # print('time_list_utc', time_list_utc)
    #
    # print('time_in_sec', time_in_sec)

    return time_in_sec, ups_list


plt.ion()
f, ax = plt.subplots(1)

while True:
    time, ups = i_plot()
    ax.plot(time, ups, markersize=1)
    plt.ylabel('No of Upvotes')
    plt.xlabel('Time in sec from post creation')
    ax.set_title("Plot for 'https://redd.it/5nq244'")
    ax.set_ylim(ymin=0)
    ax.set_xlim(xmin=0)
    plt.show()
    plt.pause(1)
