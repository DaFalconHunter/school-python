# Celebrity Questionnaire

# Place quiz in a while True loop to make it go back to the start:
print("================================================================")
while True:
    # Welcome the celebrity:
    name = input("Please enter your name: ").title()

    response = input("Hello " + name + "! How are you doing? Enter (G)ood or (B)ad: ").lower()
    if response == "g":
        print("Glad to hear it! Let's get on with the questions!")
    else:
        print("Aw, too bad, but you'll be just fine. Let's get on with the questions!")

    # Start the questions:

    fav_food = input("Q1) What is your favorite food? ").lower()
    print("So you like " + fav_food + "? That's delish!")

    fav_animal = input("Q2) What is your favorite animal? ").title()
    print("Ah nice! My favorite animal is the Peregrine Falcon.\nDid you know that it can reach speeds of 200 mph in a dive?")

    fav_singer = input("Q3) Who is your favorite singer/group? ").title()
    if fav_singer == "coldplay":
        print(fav_singer + "? You're my man, man! My bro! Coldplay is the best!")
    else:
        print(fav_singer + "? Oh, erm, yeah sure! " + fav_singer + " has... nice songs!\nBut no one beats Coldplay!!! No one at all!")

    fav_drink = input("Q4) What do you like to drink? ").title()
    print("Glad to hear it! Must be a really nice drink, " + fav_drink + ".")

    # Print results:

    finisher = input("""----------------------------------------------------------------
So then """ + name + """, here are your results:
Q1) What is your favorite food?: 
""" + fav_food + """
Q2) What is your favorite animal?:
""" + fav_animal + """
Q3) Who is your favorite singer/group?:
""" + fav_singer + """
Q4) What do you like to drink?:
""" + fav_drink + """
In the meantime, feel free to take this questionnaire again.
Just enter (R)estart or (F)inish: """).lower()

    # Logic to make the quiz restart:
    if finisher == "r":
        print("================================================================")
        continue
    print("Over and out!")
    break
