quantity = int(input("How many numbers do you want calculated? "))
nums = []
for i in range(quantity):
    num = int(input("Enter a number: "))
    nums.append(num)

# Using builtin function:
total = sum(nums)

# Using normal python:
total = 0
for i in range(len(nums)):
    total += nums[i]
    
print(f"Total: {total}")
average = total / quantity
print(f"Average: {average}")

