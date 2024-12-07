# PiOS Lite - A Simple Python-Based OS

### PiOS Lite is a lightweight, Python-based operating system with basic utilities and user management. It offers time display, text editing, system updates, backups, and restores—all in a simple interface.

## Components:
- Installer (installer.py): Guides you through the installation process.
- Main OS (pios.py): Runs the system with features like time display, text editor, and system tools.
- Updater (updater.py): Fetches and installs updates from a USB drive while preserving user data.
- Backup/Restore (backup.py, pirestore.py): Create and restore system backups, or wipe the system to start fresh.
## How It Works:
1. Installation: Run installer.py to set up PiOS Lite and create a user account with a hashed password.
2. Using PiOS Lite: Access the time display, text editor, and system tools through pios.py.
3. Updating: Use updater.py to update the system with files from a USB drive.
4. Backup/Restore: Back up system files with backup.py, restore from a backup, or wipe the system with pirestore.py (requires login).