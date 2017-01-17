import datetime

import matplotlib.pyplot as plt
import pymongo

client = pymongo.MongoClient("mongodb://moulick:1011sailboat@localhost")
reddit_db = client.reddit
collection = reddit_db.whatsapp
print('Database Ok')

created = (datetime.datetime(2017, 1, 13, 14, 22, 1) - datetime.datetime(1970, 1, 1)).total_seconds()
UPVOTES = {'ups': True,
           'time': True,
           '_id': False}
ups_list = []
time_list = []

time_list_utc = []
time_in_sec = []
projects = collection.find(projection=UPVOTES)
for project in projects:
    ups_list.append(project['ups'])  # Append upsvotes
    time_list_utc.append(project['time'])  # Append
    time_in_sec.append((project['time'] - datetime.datetime(1970, 1, 1)).total_seconds() - created)
print('ups_list', ups_list)
print('time_list_utc', time_list_utc)
print('time_list', time_list)

print('time_in_sec', time_in_sec)
f, ax = plt.subplots(1)
ax.plot(ups_list, time_in_sec)
plt.ylabel('No of Upvotes')
plt.xlabel('Time in sec from post creation')
ax.set_title('Plot for ')
ax.set_ylim(ymin=0)
ax.set_xlim(xmin=0)

plt.show(1)

# Check if time is in increasing order to verify time data
# if sorted(time_in_sec) == time_in_sec:
#     print('ok')
# else:
#     print('not ok')
