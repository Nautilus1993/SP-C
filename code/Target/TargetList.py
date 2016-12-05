#!/usr/bin/python
import sys, os
import string

def initFakeWebList():
    fakeWebList = []
    with open("./Target/fakeWeb") as f:
        str = f.read()
        fakeWebList = str.split('\n')
    return fakeWebList

def initFileList():
    fileList = []
    with open("./Target/fileExtension") as f:
        str = f.read()
        fileList = str.split("\n")
    return fileList

def initUserList():
    userList = []
    with open("./Target/protectedUser") as f:
        str = f.read()
        userList = str.split("\n")
    return userList

def trigger(targetList, wordList):
    '''
    :param targetList: List include malicious elements.
    :param wordList:  Tweet in list format.
    :return: if a tweet contain the items in target list.
    '''
    for t in targetList:
        for w in wordList:
            if t in w:
                return True
    return False