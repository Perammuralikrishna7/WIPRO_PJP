
def ispalindrome(S):
    return(S==S[::-1])
        
        


def count_the_vowels(name):
    l=len(name)
    sum=0
    for i in range(l):
        if(name[i] in ['a','e','i','o','u']):
            sum+=1
        elif(name[i] in ['A','E','I','O','U']):
            sum+=1
    return sum



def frequency_of_letters(name):
    freq={}
    for i in name:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq





