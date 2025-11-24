#OOPS

# Class: a class is a blueprint/template
# class Student:
#     pass
#What is an object: instance of a class
# s1=Student()
# s2=Student()
#Constructor
# __init__

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
s1= Student("Prabhjot", 90)
print(s1.name, s1.marks)