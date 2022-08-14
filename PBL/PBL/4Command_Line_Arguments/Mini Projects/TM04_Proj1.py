from sys import argv

like = argv[1].split('-')
dislike = argv[2].split('-')
l = argv[3].split('-')
h = 0
for i in l:
    if i in like:
        h += 1
    elif i in dislike:
        h -= 1
print("Final happiness is "+str(h))