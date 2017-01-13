import praw

# reddit = praw.Reddit(client_id='*',
# client_secret='*',
# user_agent='*',
# username='*',
# password='*')

reddit = praw.Reddit('XD')

# create a reddit instance with site from ./praw.ini

print('Read only:', reddit.read_only)  # Check if read_only

submission = reddit.submission(
    url='https://www.reddit.com/r/pics/comments/5njti8/if_you_didnt_believe_it_was_a_cake_well_heres_the/')
print('ok')
# assume you have a Reddit instance bound to variable `reddit`
print(submission.title)  # to make it non-lazy
# pprint.pprint(vars(submission))

score = submission.score
upvote_ratio = submission.upvote_ratio

ups = score * upvote_ratio
downs = score * (1 - upvote_ratio)
print('score:', score)
print('ratio:', upvote_ratio)
print('ups:', round(ups))
print('downs:', round(downs))
