# def greet (name):
#     return print(f"hello, {name}")
# greet('teja')

# def greet(name='teja'):
#     return f"hello,{name}"
# # print(greet())
# print(greet('ravi'))

# a=[1,2,3,4,5]
# b=a[2:]
# print(b)

# def rotate_list(lis,s):
#     return print(lis[s:]+lis[:s])

# rotate_list([1,2,3,4,5],2)

# def counttt(a):
#     countt={}
#     for i in a:
#         if i not in countt:
#             countt[i]=1
#         else:
#             countt[i]+=1
            
#     return print(countt)
# counttt([1,2,2,3,3,3])

#  Example 2C: Find Pairs that Sum to Target

# def find_pair_target(nums):
#     res=[]
#     target=9
#     for i in nums:
#         for j in nums:
#             if i+j==target:
#                 res.append((i,j))
#     return print(res)
    
# find_pair_target([1,2,3,4,5])


# nums=[1,2,3,4,5]
# target=7
# for i in nums:
#     for j in nums:
#         if i+j==target:
#             print(i,j)

# for accessing dict

# def teja(**ar):
#     for key,value in ar.items():
#         # print('ready')
#         print(f"{key}:{value}")
# teja(name='teja',age=21, clas='xv')

# def print_details(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_details(name="Teja", age=25, city="Hyderabad")
# # name: Teja
# # age: 25
# # city: Hyderabad

# def is_pali(word):
#     return word==word[::-1]

# def find_pali(words):
#     return print([w for w in words if is_pali(w)])

# find_pali(['level','mam','madam','anakonda'])



