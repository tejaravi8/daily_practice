# Replace Each Element with Its Square
# Example: [1, 2, 3] → [1, 4, 9]

nums=[1,2,3]
sqr_num = []
for i in nums:
    if i not in sqr_num:
        sqr_num.append(i**2)
print(sqr_num)