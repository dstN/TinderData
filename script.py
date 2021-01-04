import json
import os
from datetime import datetime


def year(s):
    return s[:4]


currentYear = datetime.now().year
firstDayofSwiping = '20xx'
swipeLike = 0
swipePass = 0
matches = 0
messageSent = 0
messageReceived = 0
appOpen = 0

mostMatchesInDay = 0
mostPassesInDay = 0
mostLikesInDay = 0
mostMessagesInDay = 0
mostMessagesRecievedInDay = 0
mostAppOpenInDay = 0

with open('data.json', 'r') as f:
    data = json.load(f)
    firstDayofSwiping = list(data["Usage"]["swipes_likes"].keys())[0]
    for key in data["Usage"]["swipes_likes"]:
        swipeLike += data["Usage"]["swipes_likes"][key]
        if int(data["Usage"]["swipes_likes"][key]) > mostLikesInDay:
            mostLikesInDay = int(data["Usage"]["swipes_likes"][key])

    for key in data["Usage"]["swipes_passes"]:
        swipePass += data["Usage"]["swipes_passes"][key]
        if int(data["Usage"]["swipes_passes"][key]) > mostPassesInDay:
            mostPassesInDay = int(data["Usage"]["swipes_passes"][key])

    for key in data["Usage"]["matches"]:
        matches += data["Usage"]["matches"][key]
        if int(data["Usage"]["matches"][key]) > mostMatchesInDay:
            mostMatchesInDay = int(data["Usage"]["matches"][key])

    for key in data["Usage"]["messages_sent"]:
        messageSent += data["Usage"]["messages_sent"][key]
        if int(data["Usage"]["messages_sent"][key]) > mostMessagesInDay:
            mostMessagesInDay = int(data["Usage"]["messages_sent"][key])

    for key in data["Usage"]["messages_received"]:
        messageReceived += data["Usage"]["messages_received"][key]
        if int(data["Usage"]["messages_received"][key]) > mostMessagesRecievedInDay:
            mostMessagesRecievedInDay = int(
                data["Usage"]["messages_received"][key])

    for key in data["Usage"]["app_opens"]:
        appOpen += data["Usage"]["app_opens"][key]
        if int(data["Usage"]["app_opens"][key]) > mostAppOpenInDay:
            mostAppOpenInDay = int(data["Usage"]["app_opens"][key])

totalSwipes = swipeLike + swipePass
numYears = int(currentYear) - int(year(firstDayofSwiping))
if numYears != 0:
    numDays = numYears * 365
    swipesPerDay = totalSwipes / numDays
    appOpenPerDay = appOpen / numDays
else:
    numDays = 365
    swipesPerDay = totalSwipes / numDays
    appOpenPerDay = appOpen / numDays
    
print('Total number of swipes = ', totalSwipes)
print('Total number of swipe likes = ', swipeLike)
print('Total number of swipe passed = ', swipePass)
print('Total number of matches = ', matches)
print('Total number of messages sent = ', messageSent)
print('Total number of messages recieved = ',messageReceived)
print('Total number of times opening Tinder = ', appOpen)

print('\n')
print('Match percent rate = ', round(((matches / swipeLike) * 100), 2), '%')
print('Swipe like to swipe pass percent rate =', round(
    ((swipeLike / (swipeLike+swipePass)) * 100), 2), '%')
print('First day of swiping = ', firstDayofSwiping)
print('Average swipes per day = ', round(swipesPerDay, 2))
print('Average times opening tinder a day = ', round(appOpenPerDay, 2))

print('\n')
print('Most times opening Tinder in a day = ', mostAppOpenInDay)
print('Most most matches in a day = ', mostMatchesInDay)
print('Most likes in a day = ', mostLikesInDay)
print('Most passes in a day = ', mostPassesInDay)
print('Most messages in a day = ', mostMessagesInDay)
print('Most messages recieved in a day = ', mostMessagesRecievedInDay)
