import os
import shutil
import time

def check_for_updates():
    usb_path = input("Insert USB and specify the drive path (e.g., E:/): ")
    update_folder = usb_path + "/OS_Updates"

    if os.path.exists(update_folder):
        print("Update folder found.")
        return update_folder
    else:
        print("No update folder found. Please check the USB drive.")
        return None

def apply_update(update_folder):
    if update_folder:
        print("Starting update...")

        # Example: Overwriting the core files of the OS (simplified for this example)
        try:
            os.makedirs("OS_Backup", exist_ok=True)
            shutil.copytree("current_os_files", "OS_Backup")  # Backup current files
            
            for filename in os.listdir(update_folder):
                src = os.path.join(update_folder, filename)
                dest = os.path.join("current_os_files", filename)
                shutil.copy2(src, dest)
                
            print("Update applied successfully!")
        except Exception as e:
            print(f"Error during update: {e}")
    else:
        print("No update folder found. Exiting update process.")

def updater():
    print("Checking for updates...")
    update_folder = check_for_updates()
    time.sleep(1)
    apply_update(update_folder)

if __name__ == "__main__":
    updater()
