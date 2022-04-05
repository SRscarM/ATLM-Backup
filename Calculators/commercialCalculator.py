'''
ATL MARATHON
NAME: SOURAV
DOC: 5/4/2022
TOPIC: Commercial Maths Calculator
'''

import math

mainLoop = True

print("***>COMMERCIAL MATHS CALCULATOR***>","\n")

def Profit():
    sp = float(input("Enter the Selling Prise ="))
    cp = float(input("Enter the Cost Prise ="))

    profit = sp - cp

    print(f"The Profit is ={profit}","\n")

def Loss():
    sp = float(input("Enter the Selling Prise ="))
    cp = float(input("Enter the Cost Prise ="))

    loss = cp - sp

    print(f"The Loss is ={loss}","\n")


def ProfitPer():
    sp = float(input("Enter the Selling Prise ="))
    cp = float(input("Enter the Cost Prise ="))

    profit = sp - cp
    profitPer = (profit*100)/cp

    print(f"The Profit% is ={profitPer}","\n")


def LossPer():
    sp = float(input("Enter the Selling Prise ="))
    cp = float(input("Enter the Cost Prise ="))

    loss = cp - sp
    lossPer = (loss * 100) / cp

    print(f"The Loss% is ={lossPer}","\n")

def SimpleInterest():
    p = float(input("Enter the Principle ="))
    r = float(input("Enter the Rate ="))
    t = float(input("Enter the Time(in years) ="))

    si = (p*r*t)/100

    print(f"The SI is ={si}","\n")

while mainLoop:

    try:

        print("***>PICK THE FORMULA***>","\n")
        print("Profit or Loss")
        print("Profit% or Loss%")
        print("Simple Interest","\n")

        formula = str(input("Write the formula (ex: Profit%,SI) = "))

        if formula == "Profit" or formula == "profit":
            Profit()
        if formula == "Loss" or formula == "loss":
            Loss()
        if formula == "Profit%" or formula == "profit%":
            ProfitPer()
        if formula == "Loss%" or formula == "loss%":
            LossPer()
        if formula == "SI" or formula == "si":
            SimpleInterest()

    except ValueError:
        print("NOTE: There was an error in the input. Please Try again.", "\n")