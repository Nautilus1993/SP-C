from Target import TargetList
import os, sys

'''
    Step 1: initialize alert level and target blacklist
'''

ALERT_LEVEL = [
    "info",
    "low",
    "medium",
    "high"
]

userList = TargetList.initUserList()
fakeWebList = TargetList.initFakeWebList()
fileExtensionList = TargetList.initFileList()

'''
    Step 2: Define class "Tweet"
'''

class Tweet:
    # todo: initialize a tweet from a given string
    def __init__(self, content):
        self.content = content
        self.alert = "info"

    def Tokenizer(self):
        # transfer a tweet from string to word list.
        wordList = self.content.split(' ')
        return wordList

class TweetReader:
    # provide the input file name when intialize a tweet reader
    def __init__(self, f):
        self.tweetList = []
        self.file = f

    def readFromFile(self):
        tweetList = []
        with open(self.file) as f:
            str = f.read()
            list = str.split("\n")
        for content in list:
            tweet = Tweet(content)
            tweetList.append(tweet)
        return tweetList
'''
    Step 3 : Classifier (input: tweet, output: alert_level)
'''

class Classifier:
    def __init__(self):
        # todo: initialize weight_vector from user input
        self.weightVector = [0.2, 0.3, 0.5]
        self.featureVector = []

    def captureFeature(self, tweet):
        wordList = tweet.Tokenizer()
        f1 = TargetList.trigger(userList, wordList)
        f2 = TargetList.trigger(fakeWebList, wordList)
        f3 = TargetList.trigger(fileExtensionList, wordList)
        self.featureVector += [f1, f2, f3]

    def computeSum(self):
        flist = self.featureVector
        wlist = self.weightVector
        totalWeight = sum([f*w for f, w in zip(flist, wlist)])
        # after each time computation, clear feature vector for next computation.
        self.featureVector = []
        totalWeight *= 10
        return totalWeight

    def alertLevel(self, sum):
        if (sum > 8):
            return "high"
        elif (5 <= sum <= 7):
            return "medium"
        elif (3 < sum < 5):
            return "low"
        else:
            return "info"

    def classify(self, tweet):
        self.captureFeature(tweet)
        sum = self.computeSum()
        tweet.alert = self.alertLevel(sum)


'''
    Step 4: Given a tweet file, generate alert result report for each tweet.
'''
class Reporter:

    def __init__(self):
        self.classifier = Classifier()
        self.tweetList = TweetReader("./Tweets/tweets").readFromFile()


    def generateReport(self):
        # write tweet alert into a file.
        index = 0
        for t in self.tweetList:
            index += 1
            print "======  Report %d ======\n" % index
            print "tweet content: " + t.content + "\n"
            print "alert level: " + t.alert

    def classify(self):
        for t in self.tweetList:
            self.classifier.classify(t)

def main():
    report = Reporter()
    report.classify()
    report.generateReport()

if __name__ == "__main__":
    main()