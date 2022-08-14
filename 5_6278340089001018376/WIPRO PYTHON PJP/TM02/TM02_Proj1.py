dict={'Jeff':'Dogs', 'David':'piano', 'Jason':'airplane'}

print("Jeff: Is afraid of",dict.get('Jeff'))
print("David: Plays the",dict.get('David'))
print("Jason: Can fly an ",dict.get('Jason'))

dict['Jeff']='heights'

dict['Jill']='dance'

print("Jeff: Is afraid of",dict.get('Jeff'))
print("David: Plays the",dict.get('David'))
print("Jason: Can fly an ",dict.get('Jason'))
print("Jill: Can hula",dict.get('Jill'))