file = open(
    "Python Year 11 2024-2025/Reading & Writing to Files/names.txt",
    "w",
    encoding="utf-8",
)
file.write("Bob\n")
file.write("Tom\n")
file.write("Gem\n")
file.write("Sara\n")
file.write("Tim\n")

"""
file = open(
    "Python Year 11 2024-2025/Reading & Writing to Files/names.txt",
    "r",
    encoding="utf-8",
)
contents = file.read()
print(contents)
file.close()
"""

name = input("Please enter another name to add: ")
file.write(name)
file.close()