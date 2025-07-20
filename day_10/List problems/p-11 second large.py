# Find the second largest number in a list (without sorting).

listt=[2,1,3,5,7]

first=0
second=listt[0]
for i in listt:
    if second<=i:
        second=first
        first=i
print(second)  # 5

# Bubble_sort_method

for i in range(0,len(listt)):
    for j in range(i+1,len(listt)):
        if listt[i]>listt[j]:
            listt[i],listt[j]=listt[j],listt[i]
        else:
            listt[i],listt[j]=listt[i],listt[j]
            
print(listt[len(listt)-2])

#using sort method

listt.sort()
print(listt[-2:-1:])