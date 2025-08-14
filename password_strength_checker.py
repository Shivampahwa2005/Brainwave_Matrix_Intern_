import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 1
    else:
        feedback.append("Password should be at least 12 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    if score <= 2:
        strength = "❌ Weak"
        color = "red"
    elif score <= 4:
        strength = "⚠️ Moderate"
        color = "orange"
    else:
        strength = "✅ Strong"
        color = "green"

    return strength, feedback, color


def on_check():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password!")
        return

    strength, tips, color = check_password_strength(password)
    result_label.config(text=f"Password Strength: {strength}", fg=color)

    if tips:
        feedback_text = "\n".join(f"- {tip}" for tip in tips)
    else:
        feedback_text = "Your password is strong! ✅"

    feedback_label.config(text=feedback_text, fg="black")


# GUI Window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.config(bg="#f4f4f4")

title_label = tk.Label(root, text="🔒 Password Strength Checker", font=("Arial", 14, "bold"), bg="#f4f4f4")
title_label.pack(pady=10)

entry = tk.Entry(root, width=30, font=("Arial", 12), show="*")
entry.pack(pady=10)

check_button = tk.Button(root, text="Check Strength", command=on_check, font=("Arial", 12, "bold"), bg="#4CAF50", fg="white")
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f4f4f4")
result_label.pack(pady=10)

feedback_label = tk.Label(root, text="", font=("Arial", 10), bg="#f4f4f4", justify="left")
feedback_label.pack(pady=5)

root.mainloop()
