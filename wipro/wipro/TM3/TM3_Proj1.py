#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def sortAllColors(given_string):
    color_list=given_string.split("-")
    color_list.sort()
    srt=""
    print("Sorted colors are:")
    
    for color in color_list:
        srt=srt+color
        srt=srt+" "
        
    srt=srt.strip()
    colors=srt.replace(" ","-")
    print(colors)

user_string=input("Enter colors:")
if __name__=='__main__':
    sortAllColors(user_string)

