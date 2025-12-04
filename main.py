import hashlib
import json
import os
from emailValidation import email_validation
from drive import upload_file, view_files, delete_file

# save data user with  dictionary
users = {}
username = ""
def load_users():
    global users
    with open('users.json', 'r') as f:
        users = json.load(f)
def sign_up():
    global users
    while True:
        if not os.path.exists("users.json"):
            with open('users.json', 'w') as f:
                json.dump({}, f)
        load_users()
        username = input("Enter username: ")
        if username in users:
            print("Username already exists. Please choose another.")
            continue
        elif not username.isalnum() or len(username) < 3:
            print("Username must be at least 3 characters long and alphanumeric.")
            continue
        elif len(username) > 20:
            print("Username must be at most 20 characters long.")
            continue
        while True:
            email = input("Enter email: ")
            if email_validation(email) == True:
                break
        while True:
            password = input("Enter password: ")
            if len(password) < 8:
                print("Password must be at least 8 characters long.")
                continue
            elif len(password) > 64:
                print("Password must be at most 64 characters long.")
                continue
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            users[username] = {
    "email": email, 
    "password": hashed_password
}
            break
        with open('users.json', 'w') as f:
            json.dump(users, f, indent=4, ensure_ascii=False)
            print("User registered successfully!")
            users = {username: users[username]}  # Keep only the current user in memory
            break

def login():
    global users
    if not os.path.exists("users.json"):
        print("No users registered yet. Please sign up first.")
        return False, ""
    elif os.path.getsize("users.json") == 0:
        print("No users registered yet. Please sign up first.")
        return False, ""
    load_users()
    if users == {}:
        print("No users registered yet. Please sign up first.")
        return False, ""
    while True:
        username = input("Enter username: ")
        if username not in users:
            print("Username not found")
            return False, ""
        else:
            break
    while True:
        email = input("Enter email: ")
        if users[username]["email"] != email:
            print("Email not found")
            return False, ""    
        else:
            break
    password = input("Enter password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in users and users[username]["email"] == email and users[username]["password"] == hashed_password:
        print("Login successful! \nWelcome,", username)
        users = {username: users[username]}  # Keep only the current user in memory
        return True, username
    else:
        print("Invalid credentials. Please try again.")
        return False, ""

def main():
    global username
    while True:
        print("Welcome to the Application")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
        try:
            choice = int(input("Choose an option: "))
        except KeyboardInterrupt:
            print("\nExiting the application. Goodbye!")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == 1:
            try:
                sign_up()
            except KeyboardInterrupt:
                print("\nExiting the application. Goodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
            continue
        elif choice == 2:
            try:
                status, username = login()
                if status == True:
                    app()  
            except KeyboardInterrupt:
                print("\nExiting the application. Goodbye!")
                break
            except Exception as e:
                print(f"An error occurred: {e}")
                continue
        elif choice == 3:
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

def app():
    while True:
        choice = input(f"""This is the menu on your aplication
1. Cloud Storage
2. Exit                       
Choose an option: """)
        if choice == '1':
            while True:   
                    print("""Welcome to Cloud Storage!
This is the menu on your Cloud Storage application
1. Upload File
2. View Files
3. Delete File
4. Exit""")
                    choice = input("Choose an option: ")
                    if choice == '1':
                        upload_file(username)
                    elif choice == '2':
                        view_files(username)
                    elif choice == '3':
                        delete_file(username)
                    elif choice == '4':
                        break
                    else:
                        print("Invalid option. Please try again.")
                        continue
        elif choice == '2':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
        
main()