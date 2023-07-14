email = 'tariq@azmail.co.uk'
password = 'P_5*Kl@8'

for attempt in range(4):
    input_email = input('Enter your email address: ')
    input_password = input('Enter your password: ')
    if input_email != email or input_password != password:
        print('Please try again')
    elif input_email == email or input_password == password:
        print('Success!')
        break
