# Write a Python program that simulates a simple lottery system:
# Generate 5 random numbers between 1 and 50.
# Store them in a list.
# Display the winning numbers.
# Sample Output:
# Winning Numbers: [5, 12, 27, 38, 44]
# Your Numbers: [3, 12, 27, 40, 45]
# Matched: 2 numbers

import random
lottery=[]
a = random.randint(1,50)
b = random.randint(1,50)
c = random.randint(1,50)
d = random.randint(1,50)
e = random.randint(1,50)
list1=[a, b, c, d, e]
for i in list1:
    lottery.append(i)

a1=int(input("enter your number1 :"))
b1=int(input("enter your number2 :"))
c1=int(input("enter your number3 :"))
d1=int(input("enter your number4 :"))
e1=int(input("enter your number5 :"))
list2=[a1, b1, c1, d1, e1]
my_gusses = []
for i in list2:
    my_gusses.append(i)

guesses=0
for i in list1:
    for j in list2:
        if i==j:
            guesses+=1
        else:
            pass
print("Winning munbers",lottery)
print("your numbers",my_gusses)
print("Right guesses :",guesses)