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
list1=[]
while True:
    try:
        user = next(users)
    except tweepy.TweepError:
        time.sleep(60*15)
        user = next(users)
    except StopIteration:
        break
    list1.append(user.screen_name)

    print "list1",list1
users = tweepy.Cursor(api.followers, screen_name=person2).items()
list2=[]
while True:
    try:
        user = next(users)
    except tweepy.TweepError:
        time.sleep(60*15)
        user = next(users)
    except StopIteration:
        break
    list2.append(user.screen_name)

    print "list2",list2

result =[]
for element in list1:
        if element in list2:
         result.append(element)


print "mutual followers", result
