#Dictionary in python:
# A dictionary in python is a collection of key value pairs. 
# It is used to store data in a way to that allows fast retrevial based on keys
# unordered
# indexing by keys
# Mutable
# Follows insertion order
# Do not store duplicate values

# student = {
#     "name":"Prabhjot",
#     "age":18,
#     "course":"AIFT"
# }
# print(student)
# print(student["name"])
# print(student.get("age"))
# student["email"]="abc@gmail.com"

#update
# student["age"]=20
# print(student)

#Deleting
# student.clear()   #clears all the values 
# student.pop("email")
# del student["course"]
# print(student)


# for key in student.keys():
#     print(key)
# for value in student.values():
#     print(value)

# for key,value in student.items():
#     print(key,": ",value)


# def freq_count(nums):
#     freq={}
#     for n in nums:
#         freq[n]=freq.get(n,0)+1
#     return freq
# arr = [1,2,1,2,2,3,3,4,2]
# print(freq_count(arr))

# marks={
#     "stud1": 80,
#     "stud2": 85,
#     "stud3": 90,
#     "stud4" : 88
# }
# for key,value in marks.items():
#     if value == max(marks.values()):
#         print(f"{key}:{value}")

# brillient=max(marks,key=marks.get)          #alternative
# print("brillient student is ",brillient,"marks are :",marks[brillient])


# s1="Programming"
# s1.lower()
# def freq_count(s1):
#     freq={}
#     for n in s1:
#         freq[n]=freq.get(n,0)+1
#     return freq
# print(freq_count(s1))


# d1={
#     "a1":2,
#     "b1":3
# }
# d2={
#     "a1":4,
#     "c1":8
# }









# HW 
# Create a dictionary of 5 students with marks. Find average marks.
# marks={
#     "stud1": 80,
#     "stud2": 85,
#     "stud3": 90,
#     "stud4": 88,
#     "stud5": 89
# }
# sum=0
# for value in marks.values():
#     sum+=value
# no_of_student= len(marks)
# avg_marks=sum/no_of_student
# print(avg_marks)


# Write a program to check if two dictionaries are equal.
# d1={
#     "a1":2,
#     "b1":3,
#     "c1":6
# }
# d2={
#     "a1":4,
#     "b1":6,
#     "c1":8
# }
# if d1==d2:
#     print("Both dictionaries are equal")
# else:
#     print("try again")

# Write a Python code to remove duplicate values from a dictionary.
# marks={
#     "stud1": 80,
#     "stud2": 85,
#     "stud3": 90,
#     "stud4": 88,
#     "stud5": 90
# }
# unq_dict={}
# for key, value in marks.items():
#     if value not in unq_dict.values():      # Check if value already exists in new dictionary
#         unq_dict[key] = value
# print(unq_dict)


# Count words in a sentence using dictionary
# s1="Hi my name is prabhjot"
# s1.lower()
# def freq_count(s1):
#     freq={}
#     for n in s1:
#         freq[n]=freq.get(n,0)+1
#     return freq
# print(freq_count(s1))

