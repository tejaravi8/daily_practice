# Find the sum of all positive numbers in a list.
# Example: [2, -4, 5, -7, 8] → 2 + 5 + 8 = 15

num=[2,-4,5,-7,8]
sum=0
for i in num:
    if 0<i:
        sum+=i
print(sum)
