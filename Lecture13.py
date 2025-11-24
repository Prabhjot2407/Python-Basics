# Tuple, Set, Dictionary:

# Tuple : it is ordered , immutable collection in python. 
# elements can be of different data types
# represented by ()

# t = ("kuch bhi", "kuch ni", "sab kuch", 10, 20, 30, 1.55)
# print(t)
# print(len(t))

# t = (10, 20, 20, 30, 30, 30)
# print(max(t))
# print(t.count(30))
# print(t.index(20))

# print("sum :", sum(t))

# x = 30
# print(x in t)

# unique = tuple(set(t))
# print(unique)


### printing string in alphabetical order without using .sort
s1 = "abcDEF"
s2 = "SpiderMan"
merged = s1 + s2
merged = merged.lower()
print(merged)
chars = list(merged)

n = len(chars)
for i in range(n):
    for j in range(0, n-i-1):
        if(chars[j] > chars[j+1]):
            chars[j], chars[j+1] = chars[j+1], chars[j]
sorted_str = " ".join(chars)
print("Sorted merged strings :", sorted_str)
