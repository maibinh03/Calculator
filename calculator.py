import math

def clickbut(number, textin):
    global operator
    operator = operator + str(number)
    textin.set(operator)

def equlbut(textin):
    global operator
    try:
        result = str(eval(operator))
    except Exception as e:
        result = "Error"
    textin.set(result)
    operator = ''

def clrbut(textin):
    global operator
    textin.set('')
    operator = ''

def advanced_math(func, textin):
    global operator
    try:
        result = func(float(operator))
        textin.set(str(result))
    except Exception as e:
        textin.set("Error")
    operator = ''

operator = ''
