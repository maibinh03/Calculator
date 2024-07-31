import math
from tkinter import Label, Entry, Button, StringVar, Toplevel
import calculator

def setup_gui(me):
    melabel = Label(me, text="MÁY TÍNH", bg='White', font=("Times", 30, 'bold'))
    melabel.pack(side='top')

    textin = StringVar()
    metext = Entry(me, font=("Courier New", 12, 'bold'), textvariable=textin, width=25, bd=5, bg='powder blue')
    metext.pack()

    button_config = {
        'padx': 14,
        'pady': 14,
        'bd': 4,
        'bg': 'white',
        'font': ("Courier New", 16, 'bold')
    }

    # Layout số
    buttons = [
        ('7', 10, 100), ('8', 75, 100), ('9', 140, 100),
        ('4', 10, 170), ('5', 75, 170), ('6', 140, 170),
        ('1', 10, 240), ('2', 75, 240), ('3', 140, 240),
        ('F', 10, 310), ('0', 75, 310), ('.', 140, 310)
    ]
    
    for (text, x, y) in buttons:
        if text == 'F':
            Button(me, text=text, command=lambda: show_advanced_math(me, textin), **button_config).place(x=x, y=y)
        else:
            Button(me, text=text, command=lambda t=text: calculator.clickbut(t, textin), **button_config).place(x=x, y=y)

    # Layout phép tính
    operators = [
        ('+', 205, 100), ('-', 205, 170), ('*', 205, 240), ('/', 205, 310)
    ]
    for (text, x, y) in operators:
        Button(me, text=text, command=lambda t=text: calculator.clickbut(t, textin), **button_config).place(x=x, y=y)

    # Layout phím xoá
    Button(me, text="CE", command=lambda: calculator.clrbut(textin), padx=14, pady=119, bd=4, bg='white', font=("Courier New", 16, 'bold')).place(x=270, y=100)
    Button(me, text="=", command=lambda: calculator.equlbut(textin), padx=151, pady=14, bd=4, bg='white', font=("Courier New", 16, 'bold')).place(x=10, y=380)


def show_advanced_math(me, textin):
    advanced_window = Toplevel(me)
    advanced_window.title("Formulas")
    advanced_window.geometry("200x250")
    advanced_window.config(bg='lightgray')

    def add_advanced_function(func, symbol):
        Button(advanced_window, text=symbol, command=lambda: calculator.advanced_math(func, textin), padx=10, pady=10, bd=4, bg='white', font=("Courier New", 12, 'bold')).pack(pady=5)

    add_advanced_function(lambda x: math.sin(math.radians(x)), 'sin') 
    add_advanced_function(lambda x: math.cos(math.radians(x)), 'cos')  
    add_advanced_function(lambda x: math.tan(math.radians(x)), 'tan') 
    add_advanced_function(lambda x: 1 / math.tan(math.radians(x)) if math.tan(math.radians(x)) != 0 else float('inf'), 'cot') # Tránh chia cho 0