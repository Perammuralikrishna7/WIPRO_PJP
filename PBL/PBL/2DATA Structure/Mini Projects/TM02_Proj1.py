dict={'Jeff':'is afraid of Dogs','David':'Plays the piano','Jason':'Can fly an airplane'}
for i in list(dict.keys()):
    print(i,':',dict[i])
print('\n')
dict['Jeff']='is afraid of heights'
dict['Jill']='Can hula dance'
for i in list(dict.keys()):
    print(i,':',dict[i])
