# Initialise question var
question_1 = ""
# Initialise loop var to True
carry_on = True
while carry_on == True:
    # Establish game menu
    print("Quiz - Main Menu")
    print(
        """
    1. Instructions
    2. Quiz
    3. Quiz
    """
    )
    # Ask for user choice
    choice = input("Choose option (Enter 1 or 2 or 3): ")
    # Selection for instructions, question or exit
    if choice == "1":
        print("Instructions: Read the question and enter your answer.")
    elif choice == "2":
        print("Start the Quiz")
        question_1 = input("What is the capital of France?: ")
        if question_1 == "Paris":
            print("Correct")
        else:
            print("Incorrect")
    elif choice == "3":
        print("Thanks for playing")
        # Setting loop variable to False kills the loop
        carry_on = False
    # Invalid input catching
    elif choice != "":
        print("Not a valid choice.  Enter 1 or 2 or 3: ")
