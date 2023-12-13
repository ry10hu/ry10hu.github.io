#Things To Know Beforehand
#
#F Strings, Functions, Modules, For Loops
#Arrays, 
#
#Importing Modules (More Functions)
import os
#Defining A Function (Makes Typing This All Out Easier)
def fetch(videolist, songlist):
    for videourl in videolist:
        os.system(f'youtubedl {videourl}')
    for songurl in songlist:
        os.system(f'youtubedl --extract-audio {songurl}')
##Download List
###When Adding Urls, Make Sure To Make It A String With '' Or "" Ex: "https://www.youtube.com/watch?v=3Z5aqsvNsLQ"
videolist = ['https://www.youtube.com/watch?v=3Z5aqsvNsLQ'
             'https://www.youtube.com/watch?v=7eUzfwyFGws'
             ''
            ]

songlist = ['https://www.youtube.com/watch?v=qP-7GNoDJ5c'
            'https://www.youtube.com/watch?v=Mq-tfxKPN6s'
            ''
           ]
##Fetch Videos And Songs
fetch(videolist, songlist)
