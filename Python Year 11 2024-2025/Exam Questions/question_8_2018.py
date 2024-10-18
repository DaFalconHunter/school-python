a = 0
b = 0
c = 0

while True:
    vote = input("Enter candidate (A, B, or C): ").lower()
    match vote:
        case "a":
            a += 1
        case "b":
            b += 1
        case "c":
            c += 1
        case "end":
            break
        case _:
            print("Please enter A, B, or C")

total = a + b + c
print(f"\n{a} votes for candidate A\n{b} votes for candidate B\n{c} votes for candidate C.")
print(f"{total} total votes.\n")