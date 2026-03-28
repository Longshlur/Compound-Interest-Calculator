import tkinter as tk
from tkinter import messagebox

# Function to calculate compound interest
def calculate_ci():
    try:
        # Taking inputs
        P = float(entry_principal.get())
        R = float(entry_rate.get())
        T = float(entry_time.get())
        N = int(entry_compound.get())

        # Convert rate into decimal
        r = R / 100

        # Formula
        A = P * (1 + r / N) ** (N * T)
        CI = A - P

        # Display result
        result_label.config(
            text=f"Total Amount = ₹{A:.2f}\nCompound Interest = ₹{CI:.2f}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values")

# Create main window
root = tk.Tk()
root.title("Compound Interest Calculator")
root.geometry("400x350")
root.resizable(False, False)

# Heading
tk.Label(root, text="Compound Interest Calculator", 
         font=("Arial", 14, "bold")).pack(pady=10)

# Input fields
tk.Label(root, text="Principal Amount (₹)").pack()
entry_principal = tk.Entry(root)
entry_principal.pack()

tk.Label(root, text="Rate of Interest (%)").pack()
entry_rate = tk.Entry(root)
entry_rate.pack()

tk.Label(root, text="Time (Years)").pack()
entry_time = tk.Entry(root)
entry_time.pack()

tk.Label(root, text="Compounding Frequency (per year)").pack()
entry_compound = tk.Entry(root)
entry_compound.pack()

# Button
tk.Button(root, text="Calculate", command=calculate_ci, 
          bg="blue", fg="white").pack(pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Run application
root.mainloop()