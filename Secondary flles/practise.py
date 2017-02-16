from time import sleep

import praw

url = 'https://redd.it/5qbkqm'

# create a reddit instance with site from ./praw.ini
reddit = praw.Reddit('XD')
print('Read only:', reddit.read_only)  # Check if read_only
# print(reddit.submission(url=url).title)
while True:
    try:
        limits = reddit.auth.limits
        print(limits)
        sleep(5)
    except Exception as e:
        print(e)
        sleep(5)
