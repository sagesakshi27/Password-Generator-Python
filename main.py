import tkinter as tk
from tkinter import messagebox
import secrets as sc
import string


def gen_pass():
    try:
        length = int(length_var.get())
    except ValueError:
        messagebox.showerror("Error", "Password length must be a number!")
        return

    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_numbers = numbers_var.get()
    use_special = special_var.get()

    # Validate options
    if not any([use_uppercase, use_lowercase, use_numbers, use_special]):
        messagebox.showerror("Error", "Select at least one character type!")
        return
    if length < 15 or length > 30:
        messagebox.showerror("Error", "Password length must be between 15 and 30!")
        return

    character_pool = ""
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_numbers:
        character_pool += string.digits
    if use_special:
        character_pool += "!@#$%^&*()-_=+[]{};:,.<>?/"

    password_chars = []
    if use_uppercase:
        password_chars.append(sc.choice(string.ascii_uppercase))
    if use_lowercase:
        password_chars.append(sc.choice(string.ascii_lowercase))
    if use_numbers:
        password_chars.append(sc.choice(string.digits))
    if use_special:
        password_chars.append(sc.choice("!@#$%^&*()-_=+[]{};:,.<>?/"))

    while len(password_chars) < length:
        password_chars.append(sc.choice(character_pool))

    sc.SystemRandom().shuffle(password_chars)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, "".join(password_chars))


root = tk.Tk()
root.title("Password Generator")
root.geometry("420x320")
tk.Label(root, text="Password Length (15–30):", font=("Arial", 10, "bold")).pack()
length_var = tk.StringVar(value="15")
length_spin = tk.Spinbox(root, from_=15, to=20, textvariable=length_var, width=5)
length_spin.pack()
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=uppercase_var).pack(
    anchor="w"
)
tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=lowercase_var).pack(
    anchor="w"
)
tk.Checkbutton(root, text="Include Numbers (0-9)", variable=numbers_var).pack(
    anchor="w"
)
tk.Checkbutton(
    root, text="Include Special Characters (!@#$...)", variable=special_var
).pack(anchor="w")
password_entry = tk.Entry(root, width=42, font=("Arial", 12))
password_entry.pack(pady=10)
generate_button = tk.Button(
    root,
    text="Generate Secure Password",
    command=gen_pass,
    bg="#4CAF50",
    fg="white",
)
generate_button.pack(pady=5)
root.mainloop()
