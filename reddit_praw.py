import praw

reddit = praw.Reddit(client_id = '1klU7HAgTZHxLg' ,
                     client_secret = 'E3XXSVXQAZVGV2GdmUxALxRi_-Q',
                     username = 'singhsidhukuldeep',
                     password = 'Kuldeep@123',
                     user_agent = 'praw')

num = input("Enter the number of reddits you want to fetch (max): ")

subreddit = reddit.subreddit('python')
hot_python = subreddit.hot(limit = int(num))

counter =1

for entry in hot_python:
    if not entry.stickied:
        print (str(counter) +": " +entry.title)
        print ("Up Votes: "+str(entry.ups)+ "    Down Votes: " +str(entry.downs)+ "   Visited by the user: " +str(entry.visited))
        print "*-"*30

        commentsCounter=1
        comments = entry.comments
        for comment in comments:
            print "     Comment " + str(commentsCounter)+ ": " + comment.body
            print ""
            commentsCounter+=1

            if len(comment.replies)>0:
                repliesCounter = 1
                replies = comment.replies
                for reply in replies:
                    print "         Reply " + str(repliesCounter) + ": " + reply.body
                    print ""
                    repliesCounter += 1

        print "\n"
        counter+=1

print "#-*"*20