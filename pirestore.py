import os
import shutil
import time
import json
import subprocess
from login import login

def list_backups(backup_location):
    # List available backups in the backup location
    try:
        backups = [f for f in os.listdir(backup_location) if os.path.isdir(os.path.join(backup_location, f))]
        if backups:
            print("Available backups:")
            for idx, backup in enumerate(backups, start=1):
                print(f"{idx}. {backup}")
            return backups
        else:
            print("No backups found.")
            return []
    except Exception as e:
        print(f"Error listing backups: {e}")
        return []

def restore_backup(backup_location, backup_choice):
    try:
        # Get the backup folder name based on user choice
        backup_folder = os.path.join(backup_location, backup_choice)
        
        if os.path.exists(backup_folder):
            print(f"Restoring from {backup_folder}...")

            # Restore system files
            core_files = ["current_os_files", "users.json", "config.json"]  # List of files to restore
            for file in core_files:
                file_backup = os.path.join(backup_folder, os.path.basename(file))
                
                if os.path.exists(file_backup):
                    if os.path.isdir(file_backup):
                        if os.path.exists(file):
                            shutil.rmtree(file)  # Remove the old directory
                        shutil.copytree(file_backup, file)  # Restore directory
                    else:
                        if os.path.exists(file):
                            os.remove(file)  # Remove the old file
                        shutil.copy2(file_backup, file)  # Restore file

            print("Restore complete!")
        else:
            print("Backup folder does not exist.")
    except Exception as e:
        print(f"Error during restore: {e}")

def wipe_and_reset():
    # Wipe the current system and start setup again
    print("Wiping PiOS Lite and starting fresh setup...")
    os.system("python installer.py")  # Launch the installer again for setup

def pirestore():
    print("Welcome to PiRestore - The Recovery Tool")

    # Ensure the user is logged in before proceeding
    if not login():
        return

    backup_location = input("Enter the backup location path (e.g., E:/Backup or /home/user/backup): ")
    
    if os.path.exists(backup_location):
        backups = list_backups(backup_location)
        
        if backups:
            restore_choice = input("Do you want to restore from a backup or wipe PiOS Lite? (Enter 'restore' or 'wipe'): ").lower()
            
            if restore_choice == 'restore':
                backup_choice = input("Enter the number of the backup to restore: ")
                try:
                    backup_choice = backups[int(backup_choice) - 1]
                    restore_backup(backup_location, backup_choice)
                except (ValueError, IndexError):
                    print("Invalid choice.")
            elif restore_choice == 'wipe':
                wipe_and_reset()
            else:
                print("Invalid option selected.")
        else:
            print("No backups available to restore.")
    else:
        print("Invalid backup location!")

if __name__ == "__main__":
    pirestore()
