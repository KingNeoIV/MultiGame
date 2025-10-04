import tkinter as tk
import ctypes
import os
import sys

# Find the correct path to the DLL

base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
dll_path = os.path.join(base_path, "mathEngine.dll")

# Load the C++ DLL

engine = ctypes.CDLL(dll_path)
engine.get_question.restype = ctypes.c_char_p # Tell Python to expect a string

def start_game():
    question.set(engine.get_question().decode())

def submit_answer():
    try:
        user_input = int(entry.get())
        result = engine.check_answer(user_input)
        feedback.set("Correct!" if result else "Try again.")
    except ValueError:
        feedback.set("Enter a valid number:")

# GUI setup

root = tk.Tk()
root.title("Mike's Multiplication Game")
root.geometry("350x200")

question = tk.StringVar()
tk.Label(root, textvariable=question, font=("Arial", 16)).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()

tk.Button(root, text="Submit", command=submit_answer).pack(pady=5)
tk.Button(root, text="Start Game", command=start_game).pack(pady=5)

feedback = tk.StringVar()
tk.Label(root, textvariable=feedback, font=("Arial", 16)).pack()

root.mainloop()
