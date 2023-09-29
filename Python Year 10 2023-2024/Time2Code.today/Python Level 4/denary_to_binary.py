# Denary to binary program

# -------------------------
# Subprograms
# -------------------------
def den_to_bin(num_to_bin):
    binary = ""
    while num_to_bin > 0:
        remainder = num_to_bin % 2
        binary += str(remainder)
        num_to_bin //= 2
    return binary[::-1]

def den_to_oct(num_to_oct):
    octal = ""
    while num_to_oct > 0:
        remainder = num_to_oct % 8
        octal += str(remainder)
        num_to_oct //= 8
    return octal[::-1]

# -------------------------
# Main program
# -------------------------
number = int(input("Enter the denary number to convert to binary: "))
print("Binary:", den_to_bin(number))

number = int(input("Enter the denary number to convert octal: "))
print("Octal:", den_to_oct(number))
