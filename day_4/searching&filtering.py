# find all even numbers

# numbers=[2, 5, 8, 11, 14]

# for i in numbers: 
#     if i%2==0: 
#         print(i)

# #  Filter out negative numbers
# # Create a new list with only non-negative numbers.
  
# numbers=[3, -1, 5, -7, 0, 2]
# non_negative=[]
# for i in numbers:
#     if i>=0:
#         non_negative.append(i)
        
# print(non_negative)

# 3.find numbers greater than X
# Print numbers greater than 8.

# numbers=[4, 9, 15, 3, 12, 7]
# x = 8

# for i in numbers:
#     if i>x:
#         print(i)
        
#  4️.Count occurrences
# Given: [1, 2, 2, 3, 4, 2, 5]
# Count how many times 2 appears.

# numbers=[1, 2, 2, 3, 4, 2, 5]
# count=0
# for i in numbers:
#     if i==2:
#         count+=1
        
# print(count)

# 5.Check if a number exists
# Given: [10, 20, 30, 40]
# Check if 25 exists in the list.

# nums = [10, 20, 30, 40]
# if 25 in nums:
#     print("25 exists")
# else:
#     print("25 does not exist")

        
# 6️.Find index of first match
# Given: [5, 10, 15, 20, 15, 30]
# Find index of first occurrence of 15.

# nums = [5, 10, 15, 20, 15, 30]
# index = nums.index(15)
# print(index)
        
# 7.remove all Zeros
# Given: [0, 1, 2, 0, 3, 0, 4]
# Create a new list without zeros.

Given=[0, 1, 2, 0, 3, 0, 4]
non_zeros=[]

for i in Given:
    if i!=0:
        non_zeros.append(i)
        
print(non_zeros)



