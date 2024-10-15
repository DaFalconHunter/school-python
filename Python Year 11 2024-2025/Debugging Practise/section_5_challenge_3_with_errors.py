email = "tariq@azmail.co.uk"
password = "P_5*Kl@8"
count = 4
while count > 0:
    userEmail = input("Please enter your email address: ")
    userPassword = input("Please enter your password: ")
    if email == userEmail and password == userPassword:
        print("Details correct, you may proceed")
        break
    else:
        print("Either your username or password is incorrect")
        count -= 1
