import tkinter as tk
from tkinter import messagebox
from main import get_clean_data

# Load merged dataframe
df = get_clean_data()

def show_result():
    """Handles user input and displays the selected result."""
    state = state_entry.get().strip().title()
    choice = choice_var.get()

    if not state:
        messagebox.showwarning("Input Error", "Please enter a state name.")
        return

    state_data = df[df['state'].str.lower() == state.lower()]

    if state_data.empty:
        messagebox.showerror("Not Found", f"State '{state}' not found in dataset.")
        return

    if choice == 1:
        value = state_data["active"].values[0]
        message = f"{state} has {value:,} active cases."
    elif choice == 2:
        value = state_data["deaths"].values[0]
        message = f"{state} has {value:,} total deaths."
    elif choice == 3:
        value = state_data["total"].values[0]
        message = f"{state} has {value:,} total cases."
    elif choice == 4:
        value = state_data["discharged"].values[0]
        message = f"{state} has {value:,} discharged cases."
    else:
        messagebox.showwarning("Invalid Selection", "Please select a valid option.")
        return

    messagebox.showinfo("Result", message)

# GUI window setup
root = tk.Tk()
root.title("COVID-19 Data Viewer")
root.geometry("400x350")
root.config(bg="#f7f9fb")

tk.Label(root, text="Enter State Name:", font=("Arial", 12), bg="#f7f9fb").pack(pady=5)
state_entry = tk.Entry(root, font=("Arial", 12))
state_entry.pack(pady=5)

choice_var = tk.IntVar()

tk.Label(root, text="Choose Option:", font=("Arial", 12), bg="#f7f9fb").pack(pady=5)
tk.Radiobutton(root, text="1. Active Cases", variable=choice_var, value=1, bg="#f7f9fb").pack(anchor="w", padx=80)
tk.Radiobutton(root, text="2. Deaths", variable=choice_var, value=2, bg="#f7f9fb").pack(anchor="w", padx=80)
tk.Radiobutton(root, text="3. Total Cases", variable=choice_var, value=3, bg="#f7f9fb").pack(anchor="w", padx=80)
tk.Radiobutton(root, text="4. Discharged", variable=choice_var, value=4, bg="#f7f9fb").pack(anchor="w", padx=80)

tk.Button(root, text="Show Result", command=show_result,
          bg="#0078d7", fg="white", font=("Arial", 12), width=15).pack(pady=20)

root.mainloop()
