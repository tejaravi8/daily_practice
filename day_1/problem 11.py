# Find the index of the first occurrence of a given number in a list.
# Example: [1, 2, 3, 2, 4], find index of 2 → 1

numbers=[1, 2, 3, 2, 4]
index=0
for i in numbers:
    if i==2:
        print('index:',index)
    index+=1
    
# for i in numbers:
#     if i==2:
#         print(i)