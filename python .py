
import tkinter as tk
from tkinter import messagebox
import secrets
import string


def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4 or length > 128:
            messagebox.showerror(
                "Error",
                "Password length must be between 4 and 128."
            )
            return

        characters = ""
        required = []

        if upper_var.get():
            characters += string.ascii_uppercase
            required.append(
                secrets.choice(string.ascii_uppercase)
            )

        if lower_var.get():
            characters += string.ascii_lowercase
            required.append(
                secrets.choice(string.ascii_lowercase)
            )

        if number_var.get():
            characters += string.digits
            required.append(
                secrets.choice(string.digits)
            )

        if special_var.get():
            characters += string.punctuation
            required.append(
                secrets.choice(string.punctuation)
            )

        if not characters:
            messagebox.showwarning(
                "Warning",
                "Please select at least one character type."
            )
            return

        if len(required) > length:
            messagebox.showerror(
                "Error",
                "Password length is too short."
            )
            return

        password_list = required + [
            secrets.choice(characters)
            for _ in range(length - len(required))
        ]

        # Shuffle characters securely
        for i in range(len(password_list) - 1, 0, -1):
            j = secrets.randbelow(i + 1)
            password_list[i], password_list[j] = (
                password_list[j], password_list[i]
            )

        password = "".join(password_list)

        password_entry.config(state="normal")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state="readonly")

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter a valid numeric length."
        )


def copy_password():
    password = password_entry.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo(
            "Copied",
            "Password copied to clipboard!"
        )
    else:
        messagebox.showwarning(
            "Warning",
            "Generate a password first."
        )


# Create main window
root = tk.Tk()
root.title("Simple Password Generator")
root.geometry("480x540")
root.resizable(False, False)
root.configure(bg="#101827")

# Application title
tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 22, "bold"),
    bg="#101827",
    fg="#60A5FA"
).pack(pady=20)

tk.Label(
    root,
    text="Create a strong and secure password",
    font=("Arial", 11),
    bg="#101827",
    fg="white"
).pack()

# Password length input
tk.Label(
    root,
    text="Password Length (4-128):",
    font=("Arial", 12, "bold"),
    bg="#101827",
    fg="white"
).pack(pady=(20, 5))

length_entry = tk.Entry(
    root,
    font=("Arial", 13),
    justify="center",
    width=10
)
length_entry.insert(0, "12")
length_entry.pack()

# Character selection options
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)

options_frame = tk.Frame(root, bg="#101827")
options_frame.pack(pady=15)

options = [
    ("Uppercase Letters (A-Z)", upper_var),
    ("Lowercase Letters (a-z)", lower_var),
    ("Numbers (0-9)", number_var),
    ("Special Characters (!@#$...)", special_var)
]

for label, variable in options:
    tk.Checkbutton(
        options_frame,
        text=label,
        variable=variable,
        font=("Arial", 11),
        bg="#101827",
        fg="white",
        selectcolor="#263449",
        activebackground="#101827",
        activeforeground="white"
    ).pack(anchor="w", pady=4)

# Generate password button
tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    font=("Arial", 12, "bold"),
    bg="#2563EB",
    fg="white",
    width=22,
    pady=8,
    cursor="hand2"
).pack(pady=12)

# Display generated password
password_entry = tk.Entry(
    root,
    font=("Consolas", 12),
    width=36,
    justify="center",
    state="readonly"
)
password_entry.pack(pady=8)

# Copy password button
tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    font=("Arial", 11, "bold"),
    bg="#059669",
    fg="white",
    width=18,
    pady=6,
    cursor="hand2"
).pack(pady=8)

# Footer
tk.Label(
    root,
    text="Developed using Python and Tkinter",
    font=("Arial", 9),
    bg="#101827",
    fg="#9CA3AF"
).pack(side="bottom", pady=12)

# Run application
root.mainloop()
root.geometry("480x540")
root.resizable(False, False)
# Open application in full screen
root.state("zoomed")
root.resizable(True, True)
root.attributes("-fullscreen", True)
