import tkinter as tk
from tkinter import messagebox
import math


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        self.current_expression = ""
        self.memory = 0

        self.display_frame = self.create_display_frame()
        self.label = self.create_display_label()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), ".": (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.buttons_frame = self.create_buttons_frame()
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

    def create_display_label(self):
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg="white", fg="black", padx=24,
                         font=("Arial", 40))
        label.pack(expand=True, fill='both')
        return label

    def create_display_frame(self):
        frame = tk.Frame(self.root, height=100, bg="white")
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg="white", fg="black", font=("Arial", 24),
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        if self.current_expression and self.current_expression[-1] not in "+-*/":
            self.current_expression += operator
            self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg="lightgrey", fg="black", font=("Arial", 20),
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_expression = ""
        self.update_label()

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()
        self.create_memory_buttons()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg="lightgrey", fg="black", font=("Arial", 20), borderwidth=0,
                           command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def evaluate(self):
        try:
            self.current_expression = str(eval(self.current_expression))
            self.update_label()
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
            self.clear()
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
            self.clear()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg="lightblue", fg="black", font=("Arial", 20), borderwidth=0,
                           command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg="lightgrey", fg="black", font=("Arial", 20),
                           borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221Ax", bg="lightgrey", fg="black", font=("Arial", 20),
                           borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def square(self):
        try:
            self.current_expression = str(eval(f"{self.current_expression}**2"))
            self.update_label()
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
            self.clear()

    def sqrt(self):
        try:
            self.current_expression = str(eval(f"{self.current_expression}**0.5"))
            self.update_label()
        except Exception as e:
            messagebox.showerror("Error", "Invalid input")
            self.clear()

    def create_buttons_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        return frame

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def create_memory_buttons(self):
        button_m_plus = tk.Button(self.buttons_frame, text="M+", bg="lightgrey", fg="black", font=("Arial", 20),
                                  borderwidth=0, command=self.memory_plus)
        button_m_plus.grid(row=1, column=0, sticky=tk.NSEW)

        button_m_minus = tk.Button(self.buttons_frame, text="M-", bg="lightgrey", fg="black", font=("Arial", 20),
                                   borderwidth=0, command=self.memory_minus)
        button_m_minus.grid(row=2, column=0, sticky=tk.NSEW)

        button_mr = tk.Button(self.buttons_frame, text="MR", bg="lightgrey", fg="black", font=("Arial", 20),
                              borderwidth=0, command=self.memory_recall)
        button_mr.grid(row=3, column=0, sticky=tk.NSEW)

        button_mc = tk.Button(self.buttons_frame, text="MC", bg="lightgrey", fg="black", font=("Arial", 20),
                              borderwidth=0, command=self.memory_clear)
        button_mc.grid(row=4, column=0, sticky=tk.NSEW)

    def memory_plus(self):
        try:
            self.memory += float(self.current_expression)
        except ValueError:
            messagebox.showerror("Error", "Invalid input")

    def memory_minus(self):
        try:
            self.memory -= float(self.current_expression)
        except ValueError:
            messagebox.showerror("Error", "Invalid input")

    def memory_recall(self):
        self.current_expression = str(self.memory)
        self.update_label()

    def memory_clear(self):
        self.memory = 0


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
