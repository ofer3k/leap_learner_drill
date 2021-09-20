print('To end the mission insert =')
name = input('name: ')
allNames = []

while name!='=':
    allNames.append(name)
    name = input('name: ')

print(allNames)