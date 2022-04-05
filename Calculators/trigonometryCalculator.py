'''
ATL MARATHON
NAME: SOURAV
DOC: 4/4/2022
TOPIC: Trigonometry Calculator
'''

import math

mainLoop = True

print("***>TRIGONOMETRY CALCULATOR***>","\n")

def Sin():
    p = float(input("Enter the perpendicular side = "))
    h = float(input("Enter the hypotenuse side = "))

    angleOne = p / h
    angleOne = angleOne * (180 / math.pi)

    print(f"The Angle is {angleOne}", "\n")

def Sec():
    p = float(input("Enter the perpendicular side = "))
    h = float(input("Enter the hypotenuse side = "))

    angleOne = h / p
    angleOne = angleOne * (180 / math.pi)

    print(f"The Angle is {angleOne}", "\n")

def Cos():
    b = float(input("Enter the adjacent side = "))
    h = float(input("Enter the hypotenuse side = "))

    angleOne = b / h
    angleOne = angleOne * (180 / math.pi)

    print(f"The Angle is {angleOne}", "\n")

def Cosec():
    b = float(input("Enter the adjacent side = "))
    h = float(input("Enter the hypotenuse side = "))

    angleOne = h / b
    angleOne = angleOne * (180 / math.pi)

    print(f"The Angle is {angleOne}", "\n")

def Tan():
    p = float(input("Enter the perpendicular side = "))
    b = float(input("Enter the adjacent side = "))

    angleOne = p / b
    angleOne = angleOne * (180 / math.pi)

    print(f"The Angle is {angleOne}", "\n")

def Cot():
    p = float(input("Enter the perpendicular side = "))
    b = float(input("Enter the adjacent side = "))

    angleOne = b / p
    angleOne = angleOne * (180 / math.pi)

    print(f"The Angle is {angleOne}", "\n")

while mainLoop:

    try:

        print("***>PICK THE FORMULA***>","\n")
        print("Sin(o) or Sec(o)")
        print("Cos(o) or Cosec(o)")
        print("Tan(o) or Cot(o)","\n")

        formula = str(input("Write the formula (ex: Sin,Cot) = "))

        if formula == "Sin" or formula == "sin":
            Sin()
        if formula == "Sec" or formula == "sec":
            Sec()

        if formula == "Cos" or formula == "cos":
            Cos()
        if formula == "Cosec" or formula == "cosec":
            Cosec()

        if formula == "Tan" or formula == "tan":
            Tan()
        if formula == "Cot" or formula == "cot":
            Cot()


    except ValueError:
        print("NOTE: There was an error in the input. Please Try again.", "\n")