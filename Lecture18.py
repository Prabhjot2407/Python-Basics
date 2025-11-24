# Filter and reduced functons
 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
oddnumbers = list(filter(lambda x:x%2 != 0, numbers))
print("The odd numbers are :", oddnumbers)

from functools import reduce
numbers = [1, 2, 3, 4]
prod = reduce(lambda x,y : x*y, numbers)
print("Product of list elements are :", prod)