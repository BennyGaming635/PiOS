import os
import shutil
import time
import json
from login import login

def get_backup_location():
    # Ask user where to store the backup (local or USB)
    backup_location = input("Enter the backup location path (e.g., E:/Backup or /home/user/backup): ")
    
    # Check if backup location is valid
    if os.path.exists(backup_location):
        return backup_location
    else:
        print("Invalid location! Exiting backup process.")
        return None

def backup_system_files(backup_location):
    try:
        # Define the core system files/folders to be backed up
        core_files = ["current_os_files", "users.json", "config.json"]  # Example system files/folders
        
        # Create a backup folder
        backup_folder = os.path.join(backup_location, f"PiOS_Backup_{time.strftime('%Y%m%d_%H%M%S')}")
        os.makedirs(backup_folder)

        # Copy system files to the backup location
        for file in core_files:
            if os.path.exists(file):
                if os.path.isdir(file):
                    shutil.copytree(file, os.path.join(backup_folder, os.path.basename(file)))
                else:
                    shutil.copy2(file, backup_folder)
        
        print(f"Backup successfully created at {backup_folder}")
    except Exception as e:
        print(f"Error during backup: {e}")

def backup():
    print("Starting PiOS Backup...")

    # Ensure the user is logged in before proceeding
    if not login():
        return

    backup_location = get_backup_location()
    
    if backup_location:
        backup_system_files(backup_location)
    else:
        print("Backup failed. Invalid location.")

if __name__ == "__main__":
    backup()
