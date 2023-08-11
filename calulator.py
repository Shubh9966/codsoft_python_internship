import tkinter as tk
from tkinter import messagebox

var = ""
A = 0
operator = ""

def button_clicked(number):
    global var
    var = var + str(number)
    the_data.set(var)

def button_add_clicked():
    global A, var, operator
    A = float(var)
    operator = "+"
    var = var + "+"
    the_data.set(var)

def button_sub_clicked():
    global A, var, operator
    A = float(var)
    operator = "-"
    var = var + "-"
    the_data.set(var)

def button_mul_clicked():
    global A, var, operator
    A = float(var)
    operator = "*"
    var = var + "*"
    the_data.set(var)

def button_div_clicked():
    global A, var, operator
    A = float(var)
    operator = "/"
    var = var + "/"
    the_data.set(var)

def button_equal_clicked():
    global A, var, operator
    var2 = var
    if operator == "+":
        a = float((var2.split("+")[1]))
        x = A + a
        the_data.set(x)
        var = str(x)
    elif operator == "-":
        a = float((var2.split("-")[1]))
        x = A - a
        the_data.set(x)
        var = str(x)
    elif operator == "*":
        a = float((var2.split("*")[1]))
        x = A * a
        the_data.set(x)
        var = str(x)
    elif operator == "/":
        a = float((var2.split("/")[1]))
        if a == 0:
            messagebox.showerror("Error", "Division by 0 Not Allowed.")
            A = ""
            var = ""
            the_data.set(var)
        else:
            x = float(A / a)
            the_data.set(x)
            var = str(x)

def button_clear_clicked():
    global A, var, operator
    var = ""
    A = 0
    operator = ""
    the_data.set(var)

guiWindow = tk.Tk()
guiWindow.geometry("320x500+400+400")
guiWindow.resizable(0, 0)
guiWindow.title("GUI Calculator")

the_data = tk.StringVar()
guiLabel = tk.Label(
    guiWindow,
    text="Label",
    anchor=tk.SE,
    font=("Cambria Math", 20),
    textvariable=the_data,
    background="#ffffff",
    fg="#000000"
)
guiLabel.pack(expand=True, fill="both")

frameOne = tk.Frame(guiWindow, bg="#000000")
frameOne.pack(expand=True, fill="both")

frameTwo = tk.Frame(guiWindow, bg="#000000")
frameTwo.pack(expand=True, fill="both")

frameThree = tk.Frame(guiWindow, bg="#000000")
frameThree.pack(expand=True, fill="both")

frameFour = tk.Frame(guiWindow, bg="#000000")
frameFour.pack(expand=True, fill="both")

buttons = [
    ("7", frameThree), ("8", frameThree), ("9", frameThree), ("/", frameThree),
    ("4", frameTwo), ("5", frameTwo), ("6", frameTwo), ("*", frameTwo),
    ("1", frameOne), ("2", frameOne), ("3", frameOne), ("-", frameOne),
    ("C", frameOne), ("0", frameFour), ("=", frameFour), ("+", frameFour)
]

for (text, frame) in buttons:
    btn = tk.Button(
        frame,
        text=text,
        font=("Cambria", 22),
        relief=tk.GROOVE,
        border=0,
        command=lambda t=text: button_clicked(t) if t.isdigit() or t == "." else
        button_add_clicked() if t == "+" else
        button_sub_clicked() if t == "-" else
        button_mul_clicked() if t == "*" else
        button_div_clicked() if t == "/" else
        button_equal_clicked() if t == "=" else
        button_clear_clicked()
    )
    btn.pack(side=tk.LEFT, expand=True, fill="both")

guiWindow.mainloop()
