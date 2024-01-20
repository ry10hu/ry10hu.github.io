#HEY! This Script Is Still In Progress And Doesn't Work
#
#Install Youtube-dl And Learn More About it Here: https://github.com/ytdl-org/youtube-dl
#Things To Know Beforehand
#
#F Strings, Functions, Modules, For Loops
#Arrays, Importing Modules (More Functions)
import os
os.system('sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl')
os.system('sudo chmod a+rx /usr/local/bin/youtube-dl')
#Defining A Function (Makes Typing This All Out Easier)
def fetch(videolist, songlist):
    for videourl in videolist:
        os.system(f'youtube-dl {videourl}')
    for songurl in songlist:
        os.system(f'youtube-dl --extract-audio {songurl}')
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
