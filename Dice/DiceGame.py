import random
import tkinter as tk

class DiceRoller:
    def __init__(self, master):
        self.master = master
        self.master.title("My Dice Rolling Application - IQDOTNET CODE")
        self.master.geometry("500x300")

        self.create_ui()

    def create_ui(self):
        frame = tk.Frame(self.master)
        frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        frame.columnconfigure(0, weight=1)

        self.result_entry = tk.Entry(frame, font=("times", 100), width=6)
        self.result_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        roll_button = tk.Button(frame, text="Roll Dice!", command=self.roll)
        roll_button.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")

        reset_button = tk.Button(frame, text="Reset", command=self.reset)
        reset_button.grid(row=1, column=1, padx=10, pady=(0, 10), sticky="nsew")

        exit_button = tk.Button(frame, text="Exit", command=self.exit_app)
        exit_button.grid(row=2, column=0, columnspan=2, pady=(0, 10))

    def roll(self):
        symbols = ["\u2680", "\u2681", "\u2682", "\u2683", "\u2684", "\u2685"]
        result = f"{random.choice(symbols)}{random.choice(symbols)}"
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, result)

    def reset(self):
        self.result_entry.delete(0, tk.END)

    def exit_app(self):
        self.master.destroy()

def main():
    root = tk.Tk()
    dice_roller = DiceRoller(root)
    root.mainloop()

if __name__ == '__main__':
    main()
#IQDOTNET CODE - By Nelson Guajardo