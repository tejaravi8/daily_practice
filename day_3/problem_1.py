# Create a List of Factorials
# Example: [1, 2, 3, 4] → [1, 2, 6, 24]

nums=[1,2,3,4]
fact=1
fact_list=[]

for i in nums:
    if i>0:
        fact*=i
        fact_list.append(fact)
        
print(fact_list)