# Remove duplicate elements from a list.
#  Example: [1, 2, 2, 3, 4, 4, 5] → [1, 2, 3, 4, 5]

numbers=[1,2,2,3,4,4,5]
new=[]
for i in numbers:
    if i not in new:
        new.append(i)
print(new)

