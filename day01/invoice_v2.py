#   Turn the invoice into a function for fun :)


def ask_name(user_input):
    """Keep asking until the user enters a valid name, then return it."""
    while True:
        name = " ".join(input(user_input).split())    # trims and collapses extra spaces

        if not name:
            print("Can't be empty")
        elif any(ch.isdigit() for ch in name):
            print("Name can't contain numbers")
        elif not all(ch.isalpha() or ch in " -'." for ch in name):
            print("Only letters, spaces, hyphens, apostrophes and periods.")
        elif len(name) <2:
            print("Name too short")
        elif len(name) > 21:
            print("Name os too long.")
        else: 
            return name.title()


def ask_age(user_input):
    """Keep asking until the user enters a integer number"""
    while True:
        try:
            return int(input(user_input))
        except ValueError:
            print("Enter a whole number.")


def ask_hour(user_input):
    """Keep asking until the user enters a integer or float number"""
    while True:
        try:
            return float(input(user_input))
        except ValueError:
            print("Must be a number.")


def ask_rate(user_input):
    """Keep asking until the user enters a integer or float number"""
    while True:
        try:
            return float(input(user_input))
        except ValueError:
            print("Must be a number.")


def total(hour, rate):
    """Return total pay. rate is per hour."""
    return hour * rate


def get_user_info():
    """Ask for the user's details and returns them as a dict."""
    user = {
        "name": ask_name("Name: "),
        "age": ask_age("Age: "),
        "hour": ask_hour("Hours worked: "),
        "rate": ask_rate("Hourly rate: "),
    }

    user["total"] = user["hour"] * user["rate"]
    return user

user = get_user_info()
print(user)