                                    #REGISTRATION AND LOGIN
                                        
                                        #REGISTRATION
                                        
users = []
user = {}

username = input("Username: ")
while len(username) > 10 or len(username) == 0:
    print("invalid username 'username should not be blank or more than 10 characters'")
    username = input("username: ")
else:
    user["Username"] = username

email = input("Email Address: ")
while len(email) == 0:
    print("email field cannot be blank")
    email = input("Email: ")
else:
    user["email"] = email

first_name = input("First Name: ")
while len(first_name) == 0:
    print("first name cannot be blank")
    first_name = input("first name: ")
else:
    user["first_name"] = first_name

last_name = input("Last Name: ")
while len(last_name) == 0:
    print("last name cannot be blank")
    last_name = input("Last Name: ")
else:
    user["last_name"] = last_name

password = input("Password: ")
while len(password) == 0:
    print("password cannot be blank")
    password = input("password: ")
    
else:
    confirm_password = input("Confirm Password: ")
    while confirm_password != password or len(password) == 0:
        print("passwords do not match")
        password = input("password: ")
        confirm_password = input("Confirm Password: ")
    else:
        print("Registration successful! You may login")
user["password"] = password
        

users.append(user)
print(user)
print(users)
# print("Registration Successful, now you may login")


                                            #LOGIN

login_email = input("Email: ")
while (login_email != users[0]["email"]):
    print("user not found")
    login_email = input("Email: ")
else:

    login_password = input("Password: ")

while (login_password != users[0]["password"]):
    print("incorrect password")
   
    login_password = input("Password ")
else:

    print("LOGIN SUCCESSFUL!")

