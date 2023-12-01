# Seconds in a day program

# -------------------------
# Subprograms
# -------------------------
def seconds_to_hours(seconds):
    return seconds / 3600


def seconds_to_minutes(seconds):
    return seconds / 60 % 60


def seconds_remaining(seconds):
    return seconds % 60


# -------------------------
# Main program
# -------------------------

print(hours, "hours", minutes, "minutes", seconds, "seconds")
