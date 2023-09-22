num_bottles = 10

while num_bottles > 0:
    print(f"There are {num_bottles} green bottles hanging on the wall, {num_bottles} green bottles hanging on the wall and if 1 green bottle should accidentally fall")
    response = int(input("How many green bottles will be hanging on the wall? "))
    if response != (num_bottles - 1):
        print("No, try again")
    else:
        num_bottles -= 1

print("There are no more green bottles hanging on the wall")