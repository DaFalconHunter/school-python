num_eggs = int(input("Enter the Number of Eggs: "))
num_boxes = int(num_eggs / 6)
num_remainder = int(num_eggs % 6)
print(f'There are {num_boxes} boxes, and {num_remainder} left over')
