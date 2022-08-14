from mod import countWord
from mod import findTime

fileName='miniproj_text2.txt'
time=findTime(fileName)

if time>12:
    print("Meeting time: ",time-12,"PM")
else:
    print("Meeting time: ",time,"AM")

print("Meeting Place :",countWord(fileName),"Street")




