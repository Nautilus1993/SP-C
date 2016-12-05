import os, sys
def initTweetList():
    tweetList = []
    with open("./Tweets/tweets") as f:
        str = f.read()
        tweetList = str.split('\n')
    return tweetList
