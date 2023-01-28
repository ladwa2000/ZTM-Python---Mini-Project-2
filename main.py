#Password Checker

username = input('Enter your username: ')
password = input('Enter your password: ')

password_length = len(password) 
password_hidden = password_length * '*'

print(f'Hey, {username}! Your password {password_hidden} is {password_length} characters long')