import csv

file = open("Python Year 11 2024-2025/Reading & Writing to Files/Working With CSV Files/Books.csv", "w", encoding="utf-8")
newrecord = "To Kill A Mockingbird, Harper Lee, 1960\n"
file.write(str(newrecord))
newrecord = "A Brief History of Time, Stephen Hawking, 1988\n"
file.write(str(newrecord))
newrecord = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
file.write(str(newrecord))
newrecord = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
file.write(str(newrecord))
newrecord = "Pride and Prejudice, Jane Austen, 1813\n"
file.write(str(newrecord))
file.close()

file = open("Python Year 11 2024-2025/Reading & Writing to Files/Working With CSV Files/Books.csv", "r", encoding="utf-8")
contents = file.read()
print(contents)
file.close()
