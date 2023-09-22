question_1 = ""
carry_on = True
while carry_on == True:
    print("Quiz - Main Menu")
    print(
        """
    1. Instructions
    2. Quiz
    3. Quiz
    """
    )
    choice = input("Choose option (Enter 1 or 2 or 3): ")
    if choice == "1":
        print("Instructions: Read the question and enter your answer.")
    elif choice == "2":
        print("Start the Quiz")
        question_1 = input("What is the capital of France?: ")
        if question_1 == "Paris":
            print("Correct")
        else:
            print("Inorrect")
    elif choice == "3":
        print("Thanks for playing")
        carry_on = False
    elif choice != "":
        print("Not a valid choice.  Enter 1 or 2 or 3: ")
