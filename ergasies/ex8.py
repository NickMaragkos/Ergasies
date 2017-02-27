import tweepy
import time
from tweepy import OAuthHandler

consumer_key = 'omb55BpigyDhlyDwQhiTpWLo7'
consumer_secret = '6CrziCaPqxMZoQVkc9hwTIItkYe7CbttZGuy0uPr8mXIwmUMRo'
access_token = '815638164530462720-kcIgHiFA86Il66WQyEavLyAAbxTZx5S'
access_secret = '1sFr1M9RbRjNXEynSJGRxvgLv4sbiXR5MmH07R02pdaWw'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

person1=raw_input('Enter the twitter username of the first person')
person2=raw_input('Enter the twitter username of the second person')

users = tweepy.Cursor(api.followers, screen_name=person1).items()
follower1=[]
while True:
    try:
        user = next(users)
    except tweepy.TweepError:
        time.sleep(60*15)
        user = next(users)
    except StopIteration:
        break
    follower1.append(user.screen_name)

    print "followers of first person",follower1
users = tweepy.Cursor(api.followers, screen_name=person2).items()
follower2=[]
while True:
    try:
        user = next(users)
    except tweepy.TweepError:
        time.sleep(60*15)
        user = next(users)
    except StopIteration:
        break
    follower2.append(user.screen_name)

    print "followers of second person",follower2

result =[]
for element in follower1:
        if element in follower2:
         result.append(element)


print "mutual followers", result
