import praw

# reddit = praw.Reddit(client_id='*',
# client_secret='*',
# user_agent='*',
# username='*',
# password='*')

reddit = praw.Reddit('XD')

# create a reddit instance with site from ./praw.ini

print('Read only:', reddit.read_only)  # Check if read_only


def friend_list(reddit_instance):
    friend_count = len(reddit_instance.user.friends())
    if friend_count == 0:
        return ('You got no friends')
    else:
        return ('You have', friend_count, 'friends, congratulations!!')


def sub_red(reddit_instance):
    print('Here is a list of all your subscribed subreddits:-')

    for i, subreddits in enumerate(reddit_instance.user.subreddits()):
        print('{:>2}'.format(i + 1), subreddits, sep=': ')


print(friend_list(reddit))
sub_red(reddit)

karma = reddit.user.karma()
print("Here's your karma subreddit wise")
name_len = max([len(str(x)) for x in karma])

print('{:{align}{width}}'.format('/r,', align='^', width=name_len), 'Comment-Karma,', 'Link-Karma')

# print('name_len:', name_len)
# Extremely dirty way to format the output
for karmaname, karm in zip(karma, karma.values()):
    comment_len = int(name_len + len('Comment-Karma,') / 2 - len(str(karmaname)))
    Link_len = int(name_len - len('Comment-Karma,') + len('Link-Karma'))
    print(karmaname,
          '{:{align}{width}}'.format(karm['comment_karma'], align='>', width=comment_len),
          '{:{align}{width}}'.format(karm['link_karma'], align='>', width=Link_len), sep='  ')

print()


def blocked(reddit_instance):
    blocked_users = reddit_instance.user.blocked()
    if len(blocked_users) == 0:
        print('You seem like a peaceful person, you haven\'t blocked anyone yet')
    else:
        print('Hear is the list of people you have blocked:-')
        for i, name in enumerate(blocked_users):
            print(i + 1, name)


blocked(reddit)
# print(reddit.user.multireddits()) #MultiReddit something

contributor_sub = list(reddit.user.contributor_subreddits())
if len(contributor_sub) == 0:
    print('You don\'t contribute to any subreddit')
else:
    print('you contribute to these subreddits')
    for i, x in enumerate(contributor_sub):
        print(i+1, ': ', x, sep='')
