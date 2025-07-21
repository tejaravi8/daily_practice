# Find the second smallest number (without sorting).

List=[1,4,5,2,3,8]
first=0
second=float('inf')

for i in List:
    if second >= i:
        second=first
        first=i
print(second)