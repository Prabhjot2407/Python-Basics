# Exception Handling

# a = 10
# b = 20
# print(a + b)
# print("This is before exception")
# c = a/0
# print("This is after exception")

# try:
#     a = 10/0
# except:
#     print("Hi my name i prabhjot")

# try:
#     num = int(input("Enter a number :"))
#     result = 10/num
#     print(result)
# except ZeroDivisionError:
#     print("You can not divide by zero")
# except ValueError:
#     print("Invalid input please enter a new number")


# Using else: jab koi exception nahi hogi tab else ke pass jaega
# try:
#     x = int(input("enter a number :"))
#     print("Result :",10/x)
# except ZeroDivisionError:
#     print("Can not divide by zero")
# else:
#     print("division is succesfull")

# HW
# Que: Write a program that takes two numbers and handles division by zero
# try:
#     x = int(input("enter first number :"))
#     y = int(input("enter second number :"))
#     result = x/y
#     print("Result", result)
# except ZeroDivisionError:
#     print("not a valid input")
# else:
#     print("division is successful")

# Que: Take user input and convert it to integer, handle if user enters invalid input or divides by zero.
# try:
#     num = int(input("Enter a number :"))
#     result = 10/num
#     print(result)
# except ZeroDivisionError:
#     print("You can not divide by zero")
# except ValueError:
#     print("Invalid input please enter a new number")

# Que: Raise an exception if a user enters a negative number.
# try:
#     x = int(input("enter a number :"))
#     if x<0:
#         raise ValueError("you entered a negative number")
#     print("The number is :", x)
# except ValueError as e:
#     print("Error :",e)

# Que : Write a program that raises an exception if marks entered are not between 0 and 100.
# try:
#     x = int(input("enter a number :"))
#     if x<0 or x>100:
#         raise ValueError("you entered an invalid number")
#     print("Number is :", x)
# except ValueError as e:
#     print("Error :",e)