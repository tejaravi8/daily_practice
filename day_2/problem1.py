# Given two lists of the same length, create a new list by picking elements alternately.
# Example:[1, 2, 3] and ['a', 'b', 'c'] → [1, 'a', 2, 'b', 3, 'c']

# a= [1,2,3]
# b=['a','b','c']
# c=[]

# for i,j in zip(a,b):
#     c.append(i)
#     c.append(j)
# print(c)

a = [1, 2, 3]
b = ['a', 'b', 'c']

new = []
for i in range(len(a)):
    new.append(a[i])
    new.append(b[i])

print(new)




