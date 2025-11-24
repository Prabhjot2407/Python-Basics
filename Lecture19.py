#OOPS

# Class: a class is a blueprint/template
# class Student:
#     pass
#What is an object: instance of a class
# s1=Student()
# s2=Student()
#Constructor
# __init__

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
# s1= Student("Prabhjot", 90)
# print(s1.name, s1.marks)

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def circumference(self):
#         return 2* 3.14 * self.radius
# c = Circle(7)
# print("Circumference of circle is :", c.circumference())

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def year_salary(self):
#         return self.salary*12
# e1=Employee("Paarth Jain", 150)
# e2=Employee("Mehak", 200)
# print(e1.name, "Yearly salary is:", e1.year_salary())
# print(e2.name, "Yearly salary is:", e2.year_salary())

# class Car:
#     def __init__(self, name, model):
#         self.name = name
#         self.model = model
# c1=Car("BMW", "M4")
# c2=Car("Porsche", "911 GT3R5")
# print(c1.name, c1.model)
# print(c2.name, c2.model)


# HW
# Que1: Product Discount System
# Create a class Product that stores:
# product name, actual price, discount percentage
# Task:Make a method that returns the final price after discount.
# class Product:
#     def __init__(self, name, price, discount):
#         self.name = name
#         self.price = price
#         self.discount = discount
#     def discountedprice(self):
#         return self.price * self.discount/100
# p1 = Product("Mobile", 50000, 10) 
# print(p1.name, p1.price, p1.discountedprice())

# Que2:  Student Result Calculator
# Create a class Student with:
# name, marks in 3 subjects (given via constructor)
# Task: Write a method to calculate total marks, percentage, and return Pass/Fail
# (Pass → percentage ≥ 40)
# class Student:
#     def __init__(self, name, m1, m2, m3):
#         self.name = name
#         self.m1 = m1 
#         self.m2 = m2 
#         self.m3 = m3
#     def calcresult(self):
#         total = self.m1 + self.m2 + self.m3
#         percentage = total / 3
#         if percentage >= 40:
#             result = "Pass"
#         else:
#             result = "Fail"
#         return total, percentage, result
# s1=Student("Prabh", 90, 91, 92)
# print(s1.name, s1.calcresult())

# Que3: Bank Account – Minimum Balance Check
# Create a class BankAccount storing:
# account holder name, current balance
# Task:
# Make methods to: deposit money, withdraw moneybut withdrawal should not allow balance to go below 500
# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance
#     def withdraw(self, amount):
#         if self.balance-amount < 500:
#             print("Minimum balance of ₹500 must be maintained")
#         else:
#             self.balance -= amount
#         return self.balance
# b1 = BankAccount("Prabhjot", 50000)
# print(b1.name, b1.deposit(1000), b1.withdraw(500))

# Que4: Distance Converter
# Create a class Distance storing a value in kilometers.
# Task: Write methods to convert it to:
# meters, centimeters, millimeters
# class Distanceconverter:
#     def __init__(self, distance):
#         self.distance = distance
#     def to_meters(self):
#         return self.distance * 1000
#     def to_centimeters(self):
#         return self.distance * 100000
#     def to_millimeters(self):
#         return self.distance * 1000000
# d1=Distanceconverter(11)
# print(d1.to_meters(), d1.to_centimeters(), d1.to_millimeters())

# QUe5: Train Ticket Fare Calculator
# Create class Ticket storing: passenger name, distance (in km)
# Task:Fare Rules:, First 5 km → ₹20/km, After 5 km → ₹15/km
# Write a method that calculates total fare based on distance.
# class Trainstoring:
#     def __init__(self, name, distance):
#         self.name = name
#         self.distance = distance
#     def fare(self):
#         if self.distance <= 5:
#             return 20*self.distance
#         else:
#             return 5*20 + 15*(self.distance-5)
# t1= Trainstoring("Prabh", 8)
# print(t1.fare())
