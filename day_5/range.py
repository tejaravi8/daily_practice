# even=0
# odd=0
# for i in range(1,10,1):
#     if i%2==0:
#         even+=i
#     else:
#         odd+=i
# total=even+odd
# print(even,odd)
# print(total)      

# string="aeroplanes"
# length=len(string)
# for i in range(0,length):
#     print(string[i])

# string="aeroplanes"
# for i in range(len(string)-1,-1,-1):
#     print(string[i])
    
# rev=""
# for i in string:
#     rev=i+rev
    
# print(rev)

# string="aeroplanes"
# concate=''
# for i in range(0,len(string),2):
#     concate+=string[i]
    
# print(len(concate))

# name='botsavanivalasa'
# vowels='aeiou'
# count=0
# for i in name:
#     if i not in vowels:
#         count+=1
        
# print(count)

# name="RaviTEJa"
# cap=[]

# for i in name:
#     if i.isupper():
#         cap.append(i)
        
# print(cap)
# print(len(cap))

# name="RaviTEJa"
# vowels="aeiou"
# count_vow=0
# low=""
# for i in name:
#     if i.islower():
#         low+=i

# for j in low:
#     if j in vowels:
#         count_vow+=1
         
# print(count_vow)

# name="RaviTEJa@"

# for i in name:
#     if not i.isalpha():
#         print(i)

# listt=[11,2,3,4,5,11,33,11]
# for i in listt:
#     if i>=10:
#         print(i)

digit=9391254093
sum=0
for i in str(digit):
    if int(i)>5:
        sum+=int(i)
    
print(sum)