jerseyandcolours = {'CSK' : 'Yellow',
'RCB' : 'Red','MI' : 'Blue','SRH' : 'Orange'}
					
print('List Of given jersey:\n')

for jersey in jerseyandcolours:
	print(jersey)
    
print('List Of given colurs:\n')   
for colours in jerseyandcolours.values():
    print(colours)

print('List Of given jersey and colours:\n')
  

for jersey,colours in jerseyandcolours.items():
    print(jersey, ":", colours)