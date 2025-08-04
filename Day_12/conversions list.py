# # List to Dictionary

# # 🎯 Case A: Two Lists → One Dictionary

# # keys = ['name', 'age', 'city']
# # values = ['Teja', 21, 'Hyderabad']
# # freq={}

# # result=dict(zip(keys,values))
# # print(result)


# # for i in range(len(keys)):
# #     freq[keys[i]]=values[i]
# # print(freq)                         #out of range error may occur

# # 🎯 Case B: List of Tuples → Dictionary

# # pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
# # d = dict(pairs)
# # print(d)

# # d={}
# # for i,j in pairs:
# #     d[i]=j
# # print(d)

# # 2. Dictionary to List Conversion

# d = {'x': 10, 'y': 20}
# # keys = list(d.keys())
# print(list(d.items()))

# 🔁 3. Nested Dictionary

# students = {
#     'Teja': {'math': 90, 'science': 85},
#     'Ravi': {'math': 80, 'science': 78}
# }
# print(list(students))
# print(students['Ravi']['math'])

# data = [
#     ('Teja', {90,8}),
#     ('Ravi',{80,65})
# ]
# d=dict(data)
# # for name , math, sci in data:
# #     d[name]={"mat":math , "sci":sci}
    
# print(d)


listt=[('a', 1), ('b', 2)]
# d=dict(listt)
# print(d)
# d={}
# for i,j in listt:
#     d[i]=j
# print(d)

# Convert ={'x': 1, 'y': 2} 
# # o=[]
# # p=[]
# a=list(Convert.keys())
# print(a)

# names=["teja","j","i"]
# marks=[{1,2,3},[3,5,7],[2,6,8]]
# a=dict(zip(names,marks))
# print(a)
# a=[ ['name', 'Teja'], ['age', 21] ]
# l={}
# for i, j in a:
#     l[i]=j
# print(l)

# Write a function that takes a deeply nested list of integers (e.g. [[1, 2, [3, 4]], 5, [6, [7, 8]]]) and returns a flat list containing all the integers.
# Input: [[1, 2, [3, 4]], 5, [6, [7, 8]]]
# Output: [1, 2, 3, 4, 5, 6, 7, 8]


# a=[[1, 2, [3, 4]], 5, [6, [7, 8]]]
# b=[]
# for i in range(len(a)):
#     if i==type(list):
#         b.extend(i)
# print(b)

# a=[[2, 3,9], [10, -2, 1], [4, 5, 6]]


# for i in range(len(a)):
#     (a[i][1])=1
# print(a)
# maxb=0
# for i in a:
#     sum=0
#     for j in i:
#         sum+=j
#     if maxb<sum:
#         maxb=sum
# print(sum)   

# count=0
# for i in a:
#     for j in i:
#         if j%2==0:
#             count+=1
# print(count)

# input:       nested=[[1, 2, [3, 4]], 5, [6, [7, 8]]]
# Output:      [1, 2, 3, 4, 5, 6, 7, 8]

# new=[]
# for i in nested:
#     if type(i)==list:
#         for j in i:
#             if type(j)==list:
#                 new.extend(j)
#             else:
#                 new.append(j)
#     else:
#         new.append(i)
# print(new)

#2.  Given a list of lists of integers, write a program to return the sublist which has the maximum sum of its elements.
# Input: [[2, 3], [10, -2, 1], [4, 5, 6]]

# nested=[[2, 3], [10, -2, 1], [4, 5, 6]]
# max=0
# a=[]
# for i in nested:
#     sum=0
#     if type(i)==list:
#         for j in i:
#             sum+=j
#     if sum>max:
#         a=i
# print(a)

# a=nested[0]
# for i in nested:
#     if sum(i)>sum(a):            #  [a]  TypeError: 'builtin_function_or_method' object is not subscriptable
#         a=i
# print(a)


# Given a nested list of numbers and a target number, replace all occurrences of the number with -1.
# Input: [[1, 2, 3], [4, 2, 5]], target = 2

# nested= [[1, 2, 3], [4, 2, 5]]
# new=[]
# target = 2
# for i in nested:
#     if type(i)==list:
#         sub_new=[]
#         for j in i:
#             if j==target:
#                 sub_new.append(-1)
#             else:
#                 sub_new.append(j)
#         new.append(sub_new)
# print(new)
            
# for i in nested:
#     sub=[]
#     for j in i:
#         if j==target:
#             sub.append(0)
#         else:
#             sub.append(j)
#     new.append(sub)
# print(new)   


# Given a list of sublists, each with at least 2 elements, sort the entire list based on the second element in each sublist.
# Input: [[1, 4], [3, 1], [5, 2]]
# Output: [[3, 1], [5, 2], [1, 4]]

# nested=[[1, 4], [3, 1], [5, 2]]
# for i in range(len(nested)):
#     for j in range(i+1,len(nested)):
#         if nested[i][1]>nested[j][1]:
#             nested[i],nested[j]=nested[j],nested[i]
# print(nested)

# Write a function to transpose a nested list (matrix) — i.e., convert rows into columns.
# matrix=[[1, 2, 3],[4, 5, 6]]

# result = []
# for i in range(len(matrix[0])):
#     new=[]
#     for j in range(len(matrix)):
#         new.append(matrix[j][i])
#     result.append(new)
    
# print(result)

# Question:
# Given a list of lists where each sublist contains marks in [Math, English, Science], calculate the average for each subject.
# Input: [[80, 70, 60], [90, 85, 75], [60, 75, 80]]
# Output: Math: 76.67, English: 76.67, Science: 71.67

# # [Math, English, Science]
# nested=[[80, 70, 60], [90, 85, 75], [60, 75, 80]]
# mat=0
# sci=0
# eng=0

# # avg=math/len(nested)

# for i,j,l in nested:
#     mat+=i
#     eng+=j
#     sci+=l
# math=mat/len(nested)
# science=sci/len(nested)
# english=eng/len(nested)
# print(math,english,science)


# # Write a function that checks if two nested lists have the same structure (same lengths and levels), even if the values differ.
# #Output: True (because structure is same)

# # nested1=[ [1, 2], [3, 4] ]  
# # nested2=[ ["a", "b"], ["c", "d"] ]

# # if len(nested1)==len(nested2):
# def check(a,b):
#     if len(a)==len(b):
#         for i in range(len(a)):
#             if type(a[i])==type(b[i]):
#                 if len(a[i])==len(b[i]):
#                     return True
#                 else:
#                     return False
#             else:
#                 return False
#     else:
#         return False
     
# # print(check([ [1, 2], [3, 4] ],[ ["a", "b"], ["c", "d"] ]))


# # Create a 10x10 multiplication table using a nested list, where table[i][j] = (i+1)*(j+1).
# # Output=[ [1, 2, 3, ..., 10],  
# #   [2, 4, 6, ..., 20],  
# #   ...
# #   [10, 20, 30, ..., 100] ]

# nested=[]
# for i in range(1,11):
#     new=[]
#     for j in range(1,11):
#         new.append(i*j)
#     nested.append(new)
# print(nested)
