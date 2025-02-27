import sys

import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    password:bytes = password.encode('utf-8')
    return bcrypt.hashpw(password, salt)

def register_user():
    while True:
        username = input("Username: ")
        if not username:
            print("Username cannot be empty")
            continue
        break
    while True:
        password = input("Password: ")
        if not password:
            print("Password cannot be empty")
            continue
        break

    save_to_file(username, password)

def save_to_file(username, password):
    with open("./../user.txt", "a") as file:
        file.write(f"{username}, {hash_password(password)} \n")

def validate_user(username, password):
    with open("./../user.txt", "r") as file:
        details = file.read()
        for line in details.split('\n'):
            stored_username, stored_password = line.split(",")
            if username == stored_username:
                return bcrypt.checkpw(password.encode("utf-8"), stored_password.encode("utf-8"))
    return False

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if validate_user(username, password):
        print("Login successful")
    else:
        print("Login not successful")

def main():
    menu = """
        1. Register
        2. Login user
        3. Logout    
    """

    choice = int(input(menu))
    match choice:
        case 1: register_user()
        case 2: login()
        case 3: sys.exit(0)
main()