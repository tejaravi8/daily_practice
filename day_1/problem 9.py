# Write a program that takes two lists and returns a new list of elements that appear in both.
# Example: [1, 2, 3, 4] and [3, 4, 5, 6] → [3, 4]

first=[1, 2, 3, 4]
second=[3, 4, 5, 6]
common=[]
for i in first:
    if i in second:
        common.append(i)
print(common)     