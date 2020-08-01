import tweepy
import numpy as np
import itertools

auth = tweepy.OAuthHandler("", "")
api = tweepy.API(auth)
friendsList=[]
followersList=[]
friendFile = open("friends.txt", "w")
followerFile = open("followers.txt", "w")
notFollowingBackFile = open("notFollowingBack.txt", "w")
youDontFollowBackFile = open("youDontFollowBack.txt", "w")
for user in tweepy.Cursor(api.friends, screen_name="", skip_status=True, count=200).items():
    line=user.screen_name+"\n"
    friendsList.append(user.screen_name)
    friendFile.write(line)

for user in tweepy.Cursor(api.followers, screen_name="", skip_status=True, count=200).items():
    followersList.append(user.screen_name)
    line=user.screen_name+"\n"
    followerFile.write(line)

dont_follow_you_back=list(set(friendsList).difference(followersList))
you_dont_follow_back=list(set(followersList).difference(friendsList))
for item in dont_follow_you_back:
    line=item+"\n"
    notFollowingBackFile.write(line)

for item in you_dont_follow_back:
    line=item+"\n"
    youDontFollowBackFile.write(line)

friendFile.close()
followerFile.close()
notFollowingBackFile.close()
youDontFollowBackFile.close()


