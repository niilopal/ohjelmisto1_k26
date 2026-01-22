names = set()
while 0 == 0:
    inp = input('Enter a name or leave blank to stop: ')
    if inp == "":
        break
    if inp in names:
        print('Existing name')
    else:
        names.add(inp)
        print('New name')
for i in names:
    print(i)