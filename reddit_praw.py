#Importing the praw
import praw

reddit = praw.Reddit(client_id = '1klU7HAgTZHxLg' ,
                     client_secret = 'E3XXSVXQAZVGV2GdmUxALxRi_-Q',
                     username = 'singhsidhukuldeep',
                     password = 'Kuldeep@123',
                     user_agent = 'praw')

keyword = raw_input("Enter your Keyword: ")
num = input("Enter the number of reddits you want to fetch (max): ")

subreddit = reddit.subreddit(keyword)

hot_python = subreddit.hot(limit = int(num))
entryCounter =1
for entry in hot_python:
    if not entry.stickied:
        print (str(entryCounter) +": " +entry.title)
        print ("Up Votes: "+str(entry.ups)+ "    Down Votes: " +str(entry.downs)+ "   Visited by the user: " +str(entry.visited))
        print "*-"*30
        entryCounter+=1


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

        entry.comments.replace_more(limit=0)
        # limiting to 15 results to save output
        for comment in entry.comments.list()[:15]:
            print(20 * '#')
            print('Parent ID:', comment.parent())
            print('Comment ID:', comment.id)
            # limiting output for space-saving-sake, feel free to not do this
            print(comment.body[:200])

        print "\n"

print "#-*"*20