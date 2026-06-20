import tkinter as tk
import random

def play_game():
    number = random.randint(1, 5)
    guess = int(entry.get())
    if guess == number:
        result.set("🎉 Correct!")
    else:
        result.set(f"❌ Wrong! The number was {number}")

root = tk.Tk()
root.title("Guess the Number Game")

tk.Label(root, text="Guess a number between 1 and 5").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Submit", command=play_game).pack()
result = tk.StringVar()
tk.Label(root, textvariable=result).pack()

root.mainloop()
