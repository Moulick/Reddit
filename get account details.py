import praw

# reddit = praw.Reddit(client_id='*',
# client_secret='*',
# user_agent='*',
# username='*',
# password='*')

reddit = praw.Reddit('XD')

# create a reddit instance with site from ./praw.ini

print('Read only :' ,reddit.read_only) #Check if read_only

friend_count = len(reddit.user.friends())
if friend_count == 0:
    print('You got no friends')
else:
    print('You have', friend_count, 'friends, congratulations!!')

print('Here is a list of all your subscribed subreddits:-')
for i, subreddits in enumerate(reddit.user.subreddits()):
    print(i+1, ':', ' ',subreddits, sep = '')

karma = reddit.user.karma()
print("Here's your karma subreddit wise")
name_len = max([len(str(x)) for x in karma])

print('{:{align}{width}}'.format('/r,', align='^', width=name_len), 'Comment-Karma,', 'Link-Karma')

#print('name_len:', name_len)
#Extremly dirty way to format the output
for karmaname, karm in zip(karma, karma.values()):
    comment_len = int(name_len + len('Comment-Karma,') / 2 - len(str(karmaname)))
    Link_len = int(name_len - len('Comment-Karma,') + len('Link-Karma'))
    print(karmaname,
          '{:{align}{width}}'.format(karm['comment_karma'], align='>', width=comment_len),
          '{:{align}{width}}'.format(karm['link_karma'], align='>', width=Link_len), sep = '  ')

print()


blocked_users = reddit.user.blocked()
if len(blocked_users) ==0:
    print('You seem like a peaceful person, you haven\'t blocked anyone yet')
else:
    print('Hear is the list of people you have blocked:-')
    for i, name in enumerate(blocked_users):
        print(i+1, name)


# print(reddit.user.multireddits()) #MultiReddit something

contributor_sub = list(reddit.user.contributor_subreddits())
if len(contributor_sub) == 0:
    print('You don\'t contribute to any subreddit')
else:
    print('you contribute to these subreddits')
    for i, x in enumerate(contributor_sub):
        print(i+1, ': ', x, sep='')

