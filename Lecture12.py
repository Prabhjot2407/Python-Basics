# def find_duplicate(s):
#     seen = set()
#     for ch in s:
#         if ch in seen:
#             return ch
#         seen.add(ch)
#     return None
# user = input("enter your name :")
# duplicate = find_duplicate(user)
# if duplicate:
#     print(f"DUPLICATE CHARACTER FOUND :{duplicate}")
# else:
#     print("NO DUPLICATE FOUND")


## only for many duplicate charachters(for practice only)
from collections import Counter
def find_all_duplicates(s):
    freq = Counter(s);
    duplicates = {ch: count for ch, count in freq.items() if count>1}
    return duplicates;
user = input("enter your name :")
duplicates = find_all_duplicates(user)
if duplicates:
    print("Duplicate character with counts :")
    for ch, count in duplicates.items():
        print(f"'{ch}'...{count} times")
else:
    print("No duplicate character found")


