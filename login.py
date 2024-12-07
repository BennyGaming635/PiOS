import json
import bcrypt
import time

def load_users():
    try:
        with open("users.json", "r") as f:
            data = json.load(f)
        return data["users"]
    except FileNotFoundError:
        print("No users file found.")
        return []

def check_credentials(username, password):
    users = load_users()
    for user in users:
        if user["username"] == username:
            if bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
                return True
    return False

def login():
    print("Please log in to continue:")
    username = input("Username: ")
    password = input("Password: ")

    if check_credentials(username, password):
        print("Login successful!")
        return True
    else:
        print("Invalid credentials. Exiting...")
        return False
