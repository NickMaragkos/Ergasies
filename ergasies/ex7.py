import tweepy
import json
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

public_tweets=api.user_timeline(screen_name =person1,count=10)
list1=[]
for tweet in public_tweets:
    print tweet.text
    list1.append(tweet.text)
    print list1,list1
list2=[]
public_tweets=api.user_timeline(screen_name =person2,count=10)
for tweet in public_tweets:
    print tweet.text
    list2.append (tweet.text)
    print list2,list2
sum1=0
for item in list1:
    p=len(item.split())
    sum1=sum1+p
print sum1
sum2=0
for item in list2:
    g=len(item.split())
    sum2=sum2+g
print sum2
if sum1>sum2:
    print "the first person had more words in his tweets"
elif sum2>sum1 :
    print "the second person had more words in his tweets"
else:
    print "the use the same amount of words"
