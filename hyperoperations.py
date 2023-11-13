import numpy as np
import time



while True:
    selected_number = input("Enter a number: 1=add, 2=multiply, 3=exponentiation,4=tetration, 5=pentation, 6=hexation: ")
    if selected_number in ['1', '2', '3', '4', '5', '6']:
        break
    else:
        print("Invalid input. Please try again.")
op = int(selected_number)



def add(a, b):
    return a + b
def multiply(a, b):
    return a * b
def exponentiation(a, b):
    return a ** b
def tetration(a, b):
    if b >= 2:
        i = 2
        print("Starting to calculate...")
        while i <= b:
            a = a ** a
            print("a at i = " + str(i) + " is " + str(a))
            i = i + 1
            print("new i:" + str(i))
        return a
    else:
        print("Error: the second number b is incorrect. Expected b to be at least 2 but got " + str(b))

def pentation(a, b):
    if b >= 2:
        i = 2
        print("Starting to calculate...")
        while i <= b:
            a = tetration(a, a)
            print("a at i = " + str(i) + " is " + str(a))
            i = i + 1
            print("new i:" + str(i))
        return a
    else:
        print("Error: the second number b is incorrect. Expected b to be at least 2 but got " + str(b))

def hexation(a, b):
    if b >= 2:
        i = 2
        print("Starting to calculate...")
        while i <= b:
            a = pentation(a, a)
            print("a at i = " + str(i) + " is " + str(a))
            i = i + 1
            print("new i:" + str(i))
        return a
    else:
        print("Error: the second number b is incorrect. Expected b to be at least 2 but got " + str(b))




if op == 1:
    print("Operation is addition")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(add(a, b))
elif op == 2:
    print("Operation is multiplication")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(multiply(a, b))
elif op == 3:
    print("Operation is exponentiation")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(exponentiation(a, b))
elif op == 4:
    print("Operation is tetration")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(tetration(a, b))
elif op == 5:
    print("Operation is pentation")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(pentation(a, b))
elif op == 6:
    print("Operation is hexation")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(hexation(a, b))