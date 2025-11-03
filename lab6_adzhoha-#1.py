### User's log in. Alisa Dzhoha. This program takes a username and password from the user, checks them against a dictionary, and assigns a security level. 09/29/2025

user_info = {'gandalf1965': 'youSh@llNotP@ss_n0', 'golumn7893' : 'myPrec1os_m1ne', 'frodoBagg1e': 'yesT0_@dventure', 'samWise123': 'f0llo0wer_444', 'legoLAS': 'best_@rcher', 'guest': 'guest'}

user_name = input('Please enter your username: ')

while user_name != None:
  if user_name in user_info.keys():
    user_password = input('Please input your password: ')
    if user_password == user_info[user_name]:
        if user_password == 'guest' and user_name == 'guest':
          security_level = '2'
        else:
          security_level = '1'
        print(f'Welcome, {user_name}! Your security level is {security_level}')
        break
    else:
      print('The password is incorrect, please try again')
  else:
    print(f'The username {user_name} is not in the system, please try again')
    user_name = input('Please enter your username: ')