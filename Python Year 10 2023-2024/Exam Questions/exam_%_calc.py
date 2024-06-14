while True:
    paper1 = int(input("Enter paper 1 score out of 50: "))
    paper2 = int(input("Enter paper 2 score out of 50: "))
    paper3 = int(input("Enter paper 3 score out of 50: "))
    total_score = paper1 + paper2 + paper3
    print(f"You scored {total_score} / 150")
    percentage = round((total_score / 150) * 100)
    print(f"Your overall percentage was: {percentage}%")
    if percentage >= 60:
        print("Pass")
    else:
        print("Retake")
    again = input("Do you want to enter another set of papers? (y/n): ").lower()
    if again == "y":
        continue
    else:
        break