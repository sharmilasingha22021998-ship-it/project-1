import tkinter as tk
from math import *

# ------------------------
# Main Calculator Window
# ------------------------
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("420x550")
root.resizable(False, False)

expression = ""

# Display Entry
input_text = tk.StringVar()
display = tk.Entry(root, font=("Arial", 20), textvariable=input_text, bd=10, relief=tk.RIDGE, justify="right")
display.grid(row=0, column=0, columnspan=6, ipadx=8, ipady=20, pady=10)


# ------------------------
# Helper Functions
# ------------------------
def button_click(item):
    """Append pressed button text to the expression."""
    global expression
    expression += str(item)
    input_text.set(expression)


def button_clear():
    """Clear the entire expression."""
    global expression
    expression = ""
    input_text.set("")


def button_equal():
    """Evaluate the expression safely."""
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except Exception:
        input_text.set("Error")
        expression = ""


# ------------------------
# Button Definitions
# ------------------------
btn_params = {"padx": 20, "pady": 20, "bd": 4, "font": ("Arial", 14)}

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('sin(', 1, 4), ('cos(', 1, 5),

    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('tan(', 2, 4), ('sqrt(', 2, 5),

    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('log10(', 3, 4), ('ln(', 3, 5),

    ('0', 4, 0), ('.', 4, 1), ('(', 4, 2), (')', 4, 3),
    ('^', 4, 4), ('π', 4, 5),

    ('Clear', 5, 0), ('=', 5, 1), ('+', 5, 2),
    ('e', 5, 3), ('abs(', 5, 4), ('!', 5, 5)
]

for (text, row, col) in buttons:
    action = lambda x=text: button_click(("pi" if x == "π" else "e" if x == "e" else x).replace("^", "**"))
    tk.Button(root, text=text, command=action, **btn_params).grid(row=row, column=col)

# Special Buttons (Clear and Equal)
tk.Button(root, text="Clear", command=button_clear, bg="orange", **btn_params).grid(row=5, column=0)
tk.Button(root, text="=", command=button_equal, bg="lightgreen", **btn_params).grid(row=5, column=1)


# Start GUI loop
root.mainloop()


