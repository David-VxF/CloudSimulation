import json
def email_validation(email):
    with open('users.json', 'r') as f:
        users = json.load(f)
    if email == "":
        print("Email doesn't empty, try again!")
    elif " " in email:
        print("Email cannot contain spaces, try again!")
    elif email.count("@") != 1:
        print("Email must contain exactly one '@', try again!")
    elif email.startswith("@") or email.endswith("@"):
        print("Email cannot start or end with '@', try again!")
    elif email.count(".") < 1:
        print("Email must contain at least one '.', try again!")
    elif email.startswith(".") or email.endswith("."):
        print("Email cannot start or end with '.', try again!")
    elif ".." in email:
        print("Email cannot contain two consecutive '.', try again!")
    elif email.index("@") > email.rindex("."):
        print("The '.' must appear after the '@', try again!")
    elif any(users[user]["email"] == email for user in users):
        print("Email is already registered, try again!")
    elif "@" in email and "." in email:
        return True
    else:
        print("Email is not valid, try again!")