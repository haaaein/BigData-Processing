def login(email,passwd,userfile):
  with open("user.txt", "r") as userfile:
    for line in userfile:
      str = line.strip().split("::")
      if email == str[0] and passwd == str[1]:
        rslt = "Login Success"
      elif email != str[0]:
        rslt = "No user information"
      elif passwd != str[1]:
        rslt = "Password mismatch"
    return rslt

user_info_file = 'user.txt'
user_email = input('Enter your email: ' )
user_passwd = input('Enter your password: ' )

print(login(user_email,user_passwd,user_info_file))
