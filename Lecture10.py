# list compression

# Syntax:
        #[expression for item in iterable if condition]


# squares = [x**2 for x in range(1, 11)]
# print(squares)

# evens = [x for x in range(1, 21) if x%2 == 0]
# print(evens)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print(matrix[1][2])

for row in matrix:
    for val in row:
        print(val, end =" ")
    print()



# num = int(input("enter a number :"))
# total = 0
# while num > 0:
#     digit = num%10
#     total += digit
#     num //= 10
# print("sum of digits :", total)
