# find duplicates

nums = [1,2,2,3,4,4,5,5,6,4]

seen = set()
duplicates = set()

for num in nums:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

print("Duplicates:", list(duplicates))


# nums=[1,2,2,3,4,4,4,5,6,4]
# seen=[]
# duplicate=[]

# for i in nums:
#     if i not in seen:
#         seen.append(i)
#     else:
#         duplicate.append(i)
        
# print(duplicate)