import tkinter as tk
from tkinter import messagebox

# Function to perform the calculation
def calculate():
    try:
        # Get input values from the user
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operator_var.get()

        # Perform the appropriate operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operation selected.")
            return

        # Display the result
        result_label.config(text=f"Result: {result}")

    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Set up the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields and labels
label1 = tk.Label(root, text="Enter the first number:")
label1.grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2 = tk.Label(root, text="Enter the second number:")
label2.grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Create operator dropdown
operator_var = tk.StringVar()
operator_var.set('+')  # Set default value
operator_label = tk.Label(root, text="Choose an operation:")
operator_label.grid(row=2, column=0, padx=10, pady=10)
operator_menu = tk.OptionMenu(root, operator_var, "+", "-", "*", "/")
operator_menu.grid(row=2, column=1, padx=10, pady=10)

# Create a button to trigger the calculation
calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()
