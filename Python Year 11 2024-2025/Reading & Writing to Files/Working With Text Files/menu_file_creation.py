print(
    """1) Create a new file
2) Display the file
3) Add a new item to the file
"""
)

choice = input("Please enter your choice (1, 2 or 3): ")
match choice:
    case "1":
        subject = input("Enter a school subject: ")
        file = open("subjects.txt", "w", encoding="utf-8")
        file.write(subject)
        file.close()
    case "2":
        file = open("subjects.txt", "r", encoding="utf-8")
        print(file.read())
        file.close()
    case "3":
        file = open("subjects.txt", "a", encoding="utf-8")
        subject = input("Enter a new school subject: ")
        file.write(f"\n{subject}")
        file = open("subjects.txt", "r", encoding="utf-8")
        print(file.read())
        file.close()
