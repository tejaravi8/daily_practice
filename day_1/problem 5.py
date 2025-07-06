# Reverse the elements of a list using a loop — don’t use slicing!
# Example: [10, 20, 30] → [30, 20, 10]


numbers=[10,20,30]
rev=[]
for i in range(len(numbers)-1,-1,-1):
    rev.append(numbers[i])
print(rev)

# numbers=[10,20,30]
# for i in range(len(numbers)-1,-1,-1):
#     print(numbers[i])