x = 0
username = 'python'
password = 'rules'
while x < 5:
    usernamea = input('Enter username: ')
    passworda = input('Enter password: ')
    if usernamea == username and passworda == password:
        print('Welcome')
        exit()
    else:
        x += 1
        if x < 5:
            print('Incorrect username or password. Please try again.')
if x == 5:
    print('Access denied')