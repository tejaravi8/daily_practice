# nums=[1,2,2,3,4,4,5]
# new=[]
# for i in nums:
#     if i not in new:
#         new.append(i)
        
# print(new)
# print(nums)

# input=[[1,2],[3,4],[5]]
# new=[]

# for list in input:
#     new += list
    
# print(new)

# for i in input:
#     for j in i:
#         new.append(j)
        
# print(new)


# input=[2,-1,3,-4,5]

# for i in input:
#     if i<0:
#         input[i]=0
# print(input)

# a=input('enter some:')
# items=['a','b','c']
# items.append('t')
# items.insert(0,a)
# print(items)

# listt=['a', 'b', 'c', 'b', 'd']
# for i in listt:
#     if i=='b':
#         listt.remove('b')
        
# print(listt)

# list=['a','b','c']
# list[2]='z'
# print(list)

# fruits=['banana', 'apple', 'mango']
# for i in range(0,len(fruits)):
#     print(fruits[i]=='apple')

# animals=['dog', 'cat', 'cat', 'bird']
# freq={}
# for i in animals:
#     if i not in freq:
#         freq[i] =1
#     else:
#         freq[i] +=1
        
# print(freq['cat'])

nums=[1, 2, 2, 3, 4, 4, 5,2]
freq={}
for i in nums:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1

a=max(freq,key=value)

print(a)