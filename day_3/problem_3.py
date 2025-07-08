# Remove All Negative Numbers in Place
# Example: [1, -2, 3, -4] → [1, 3]

nums=[1,-2,3,-4]
non_neg=[]

for i in nums:
    if i>0:
        non_neg.append(i)
        
print(non_neg)

# nums.pop(1)
# nums.pop(2)

# print(nums)