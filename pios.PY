import tkinter as tk
from tkinter import simpledialog, messagebox
import time
import subprocess

class PiOS:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Python OS")
        self.root.geometry("500x400")
        
        self.create_widgets()
        
    def create_widgets(self):
        self.time_label = tk.Label(self.root, text="Current time: " + time.strftime("%H:%M:%S"), font=("Arial", 16))
        self.time_label.pack(pady=20)
        
        self.update_time()

        self.text_editor_button = tk.Button(self.root, text="Open Text Editor", command=self.open_text_editor)
        self.text_editor_button.pack(pady=10)

        self.shutdown_button = tk.Button(self.root, text="Shutdown", command=self.shutdown)
        self.shutdown_button.pack(pady=10)

        self.terminal_button = tk.Button(self.root, text="Open Terminal", command=self.open_terminal)
        self.terminal_button.pack(pady=10)

        self.update_button = tk.Button(self.root, text="Check for Updates", command=self.run_updater)
        self.update_button.pack(pady=10)

    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text="Current time: " + current_time)
        self.root.after(1000, self.update_time)
        
    def open_text_editor(self):
        editor = tk.Toplevel(self.root)
        editor.title("Text Editor")
        
        text_area = tk.Text(editor, wrap="word", height=10, width=40)
        text_area.pack(padx=10, pady=10)

        def save_file():
            file_content = text_area.get(1.0, "end-1c")
            with open("textfile.txt", "w") as file:
                file.write(file_content)
            messagebox.showinfo("Save", "File saved successfully!")

        save_button = tk.Button(editor, text="Save", command=save_file)
        save_button.pack(pady=10)

    def open_terminal(self):
        terminal = tk.Toplevel(self.root)
        terminal.title("Terminal")
        
        def execute_command():
            command = simpledialog.askstring("Command", "Enter a command:")
            if command == "exit":
                terminal.destroy()
            else:
                messagebox.showinfo("Output", f"Executing: {command}")

        cmd_button = tk.Button(terminal, text="Execute Command", command=execute_command)
        cmd_button.pack(pady=10)

    def run_updater(self):
        print("Running the updater...")
        # This launches the updater script (updater.py)
        subprocess.run(["python", "updater.py"])

    def shutdown(self):
        messagebox.showinfo("Shutdown", "Shutting down OS...")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    os = PiOS(root)
    root.mainloop()
