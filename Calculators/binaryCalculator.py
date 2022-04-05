'''
ATL MARATHON
NAME: SOURAV
DOC: 4/4/2022
TOPIC: binary Calculator
'''

mainLoop = True

print("***>BINARY CALCULATOR<***","\n")

while mainLoop:

  #takes in two binary numbers
  numberOne = input("Enter the First binary number: ")
  numberTwo = input("Enter the Second binary number: ")

  #condition variable
  condition = input('Press A for Addition or Press S for Subtraction: ')
  baseCond = input('Press 2 for base 2,\nPress 10 for base 10,\nPress 8 for base 8,\nPress 16 for base 16: ')

  #base conditions
  if baseCond == '2':
    baseNumber = 2

  elif baseCond == '10':
    baseNumber = 10

  elif baseCond == '8':
    baseNumber = 8

  elif baseCond == '16':
    baseNumber = 16

  #error
  else:
    print('There is a Error in Your Input, Please Try again.')

  #functions
  def add(num1,num2,base):
    sum = bin(int(num1,base) + int(num2,base))
    return sum

  def sub(num1,num2,base):
    sub = bin(int(num1,base) - int(num2,base))
    return sub

  #condition for adding and subtracting
  if condition == 'A' or condition == 'a':
    print(add(numberOne, numberTwo, baseNumber))

  elif condition == 'S' or condition == 's':
    print(sub(numberOne, numberTwo, baseNumber))

  #error
  else:
    print('There is a Error in Your Input, Please Try again.')

