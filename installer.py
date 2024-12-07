import os
import time
import hashlib
import json
import subprocess

def welcome_screen():
    print("Welcome to the piOS Lite Installer")
    time.sleep(1)
    print("\nLet's begin the setup.\n")

def hash_password(password):
    # Using SHA-256 to hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def get_user_input():
    username = input("Enter your new username: ")
    password = input("Enter your new password: ")
    hashed_password = hash_password(password)
    
    user_data = {
        "username": username,
        "password": hashed_password
    }

    # Check if the 'users.json' file exists, and load it if it does
    if os.path.exists("users.json"):
        with open("users.json", "r") as file:
            data = json.load(file)
    else:
        data = []

    # Add the new user to the data
    data.append(user_data)

    # Write the updated data back to 'users.json'
    with open("users.json", "w") as file:
        json.dump(data, file, indent=4)
    
    print(f"\nSetting up {username}...")

    time.sleep(2)
    print("\nInstalling OS... Please wait.")
    time.sleep(3)
    print("\nSetup complete!")
    print(f"Welcome, {username}!\n")

def run_os():
    # After the setup completes, run the main OS (pios.py)
    print("Installation complete! Launching  piOS Lite...")
    subprocess.run(["python", "pios.py"])

def installer():
    welcome_screen()
    get_user_input()
    run_os()

if __name__ == "__main__":
    installer()
