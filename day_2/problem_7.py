# replace negative number with zero
# nums=[2,-3,5,-1]

nums=[2,-3,5,-1,5,6,-9,0]
new=[]
for i in nums:
    if i>0:
        new.append(i)
    else:
        new.append(0)
print(new)
