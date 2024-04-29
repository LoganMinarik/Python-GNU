# This is to prompt the user for there input
print("Enter a number")
num1 = input()

# Once again input the user for thier input
print("Enter another number")
num2 = input()

# DO THE MAGIC
operation = input("What operation would you like to do? (+, -, *, /)")

if operation == "+":
    print(int(num1) + int(num2))

if operation == "-":
    print(int(num1) - int(num2))

if operation == "*":
    print(int(num1) * int(num2))

if operation == "/":
    print(int(num1) / int(num2))
  
#Now to add a fail safe
if operation!= "+":
    if operation!= "-":
        if operation!= "*":
            if operation!= "/":
                print("Invalid Operation")

#end of code