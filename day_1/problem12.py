# Write a program to rotate a list by k elements to the right.
# Example: [1, 2, 3, 4, 5] rotated by 2 → [4, 5, 1, 2, 3]

numbers = [1, 2, 3, 4, 5]
k = 2
for i in range(k):
    last = numbers.pop()      
print("Rotated list:", numbers)


# numbers = [1, 2, 3, 4, 5]
# # k = 2
# rotated = numbers[-2:]+numbers[0:-2]
# print("Rotated list:", rotated)