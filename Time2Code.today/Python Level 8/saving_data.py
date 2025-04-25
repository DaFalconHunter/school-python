# Saving data program

# -------------------------
# Subprograms
# -------------------------
def load(filename):
    file = open(filename, "r")
    user = file.read()
    file.close()
    user = user.strip()
    return user


def save(user, filename):
    file = open(filename, "w")
    user = user + "\n"
    file.write(user)
    file.close()


# -------------------------
# Main program
# -------------------------
user = load("datafile.txt")
print("This program was written by", user + ".")
