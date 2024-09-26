import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(entry.get())
        
        if length < 4:
            messagebox.showerror("Error", "Password length should be at least 4 characters.")
            return

        # Characters to choose from (letters, digits, punctuation)
        all_characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate random password
        password = ''.join(random.choice(all_characters) for _ in range(length))
        
        # Display the password in the result label
        result_label.config(text=f"Generated Password: {password}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")

# Set up the main window
root = tk.Tk()
root.title("Password Generator")

# Label and input for password length
length_label = tk.Label(root, text="Enter the desired password length:")
length_label.grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

# Button to trigger password generation
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

# Label to display the generated password
result_label = tk.Label(root, text="Generated Password: ", font=("Helvetica", 12))
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
