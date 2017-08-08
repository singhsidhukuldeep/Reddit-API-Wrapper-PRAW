import praw

reddit = praw.Reddit(client_id = '1klU7HAgTZHxLg' ,
                     client_secret = 'E3XXSVXQAZVGV2GdmUxALxRi_-Q',
                     username = 'singhsidhukuldeep',
                     password = 'Kuldeep@123',
                     user_agent = 'praw')

keyword = raw_input("Enter your Keyword: ")
subreddit = reddit.subreddit(keyword)

for comment in subreddit.stream.comments():
    try:
        print(30*'_')
        print()
        parent_id = str(comment.parent())
        submission = reddit.comment(parent_id)
        print('Parent:')
        print(submission.body)
        print('Reply')
        print(comment.body)
    except praw.exceptions.PRAWException as e:
        pass