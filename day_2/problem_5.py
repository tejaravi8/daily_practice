# Write a program to find the difference between the largest and smallest element in a list.
# Example: [10, 3, 5, 6] → 10 - 3 = 7

numbers=[10,3,5,6]
largest=0
smallest=0
for i in numbers:
    if i>largest:
        largest=i
        
print(largest,smallest)


# nums = [10, 3, 5, 6]
# diff = max(nums) - min(nums)
# print("Difference:", diff)