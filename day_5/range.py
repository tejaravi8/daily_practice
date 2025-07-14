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

# digit=9391254093
# sum=0
# for i in str(digit):
#     if int(i)>5:
#         sum+=int(i)
    
# print(sum)

# list=[123,234,345,5,6,11,22,33]
# for i in list:
#     if len(str(i))==3:
#         print(i)

# list1=[1,2,3,'raviteja','pablo','charan','anya','coders','ball','pen',True,False]

# result=[]

# for i in list1:
#     if i==str(i) and len(i)>=6:
#         result.append(i)
        
# print(result)

# leng=float('inf')
# item=None
# for r in result:
#     if len(r)<leng:
#         leng=len(r)
#         item=r
        
# print(item)

# number=int(input('enter a number:'))
# fact=0
# for i in range(1,number+1):
#     if number%i==0 :
#         fact +=1
        
# if fact<=2:
#     print('prime') 
# else:
#     print('not a prime')

# name=input('enter a name:')
# rev=''

# for char in name:
#     rev=char+rev

# if name==rev:
#     print('Palindrome')
# else:
#     print('Not a palindrome')

# list=[{},[],0,0,1,9,True,False,"",False]
# a=''

# for i in list:
#     if i==False:
#         # print('dorikesav',i)
#         a+=str(i)
# print(a)
# print(len(a))

# my_list=[{'a':'apple','b':'ball','cat':1,'dictionary':2,'e':'egg'},{'a':1,'b':2 },{'ant':'more','h_many':1000}]
# new=[]
# for i in my_list:
#     if len(i)>3:
#         new.append(i)
        
# print(new)
# vowels='aeiou'
# v_count=0
# freq={}
# for item in new:
#     for i,j in item.items():
#         if j==str(j):
#             freq[i]=j

# for i,j in freq.items():
#     for alp in j:
#         if alp in vowels:
#             v_count+=1
                       
# print(v_count)                      26


# my_list=[{'a':'apple','b':'ball','cat':1,1:2,'e':'egg'},{1:'a',2:'bb' },{'ant':'more','h_many':1000}]       
# key_list=[]
# for dictt in my_list:
#     for key,value in dictt.items():
#         if key==str(key):
#             key_list.append(key)
            
# print(key_list)
# print(len(key_list))     27

# min=0
# for num in range(-1,-11,-1):
#     if num<min:
#         min=num
        
# print(min)

# listt=[1,2,3,4,5,6,2,1]
# product=1
# sum=0
# sum=listt[-1]+listt[-2]
# product=listt[-1]*listt[-2]

# print(product,sum)
# # for i in range(0,len(listt)):

# listt=[1,2,3,4,5,6,2,1]
# product=1
# sum=0
# for num in range(0,len(listt)):
#     listt[len(listt)-1]+
#     print(listt[num])

# num=2
# fact=1
# for n in range(1,num+1):
#     fact *=n
# print(fact)

# listt=[1,2,3,4,5,6,7,8,9,10]
# numm=[]
# for num in listt:
#     num = num**2
#     numm.append(num)
    
# print(numm)

# for num in range(1,11):
#     if num%2==0:
#         a= (num**(1/2))
#         print(a,num)

# teja='tteejjaa'
# repeat=''
# for i in teja:
#     if i not in repeat:
#         repeat+=i
        
# print(repeat)

# num=153
# sum=0
# for i in str(num):
#     sum += int(i)**3
    
# if sum==num:
#     print('armstrong')
# else:
#     print('not an armstrong' )

# max=0
# sec_max=0
# for i in range(1,11):
#     if i>max:
#         sec_max=max
#         max=i
#         # print(sec_max)

# print(sec_max)

# min=float('inf')
# sec_min=0
# for i in range(10,0,-1):
#     if i<min:
#         sec_min=min
#         min=i
# print(sec_min)

# listt=[3,2,3,4,1,6,7,8,9]
# min=0
# for i in listt:
#     if listt[0]>=i:
#         min=i
        
        
# print(min)

# listt=[1,2,3,4]
# small=float('inf')
# second=0
# for i in listt:
#     if i<small:
#         second=small
#         small=i
# print(second)

# ooppppppppppppppppsssssssssssssss

# class House:
#     name='teja'
#     print(name)
#     def details(self):
#         print(self)
        
#     details(1)
    
# class House:
#     name='raviteja'
#     def __init__(self,floors,cost,duration):
#         self.floors=floors
#         print(self.floors)
     
#     # def detail(self,x,y,z):
#     #     self.x=x
#     #     print(sel.x)
#     #     print(y)
#     #     print(z)   
        
# obj=House(1,2,3)
# obj.__init__('two',2,3)
# House(4,5,6)

# class Student:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
#         print(self.name)
#         print(self.roll)
#     def details(self,parent):
#         self.paren=parent
#         print(self.paren)
# s1=Student('teja',10)
# s1.details(50)
# s1.__init__('trh',7)

# class student:
#     def __init__(self):
#         self.__email="teja41863@gmail.com"
#         self.__password="12345678"
#         print(self.__email)
        
# obj=student()
# obj.__init__()
# print(obj.__email)
# print(a
# print(a)

# class teja:
#     def __init__(self):
#         self.email="ertyu"
        
# abc=teja()
# print(abc.email)

# class onlineExam:
    
#     def __init__(self):
#         self.__questions={
#             'a':'modi',
#             'b':'newdelhi',
#             'pyver':3
#             }
#         self.__marks=0
#         self.__login=False
        
#     def logintoexam(self,id):
#         if id=='v@123':
#             print('loged in successfully')
#             self.__login=True
            
#     def startexam(self):
#         if self.__login:
#             print('exam started')
#             for q in self.__questions.values():
#                 print(q)
            
#     def marks(self,answers):
#         for q,a in self.__questions.items():
#             if self.__questions[q] == answers[q]:
#                 self.__marks +=1
#         print(self.__marks,'total')
            
# obj=onlineExam()
# # i_d=input('enter id:')
# obj.logintoexam('v@123')
# obj.startexam()
# obj.marks({'a':'modi',
#             'b':'newdelhi',
#             'pyver':3})  

# class parent:
#     def __init__(self,n,m):
#         self.name=n
#         self.name2=m
#         print(self.name)
#         print(self.name2)
        
# class child(parent):
#     def call(self,i):
#         self.name=i
#         print(self.name)
        
# obj=child(3,5)
# obj.call(8)

# output based on for,while

# for i in range(3):
#     print(i)

# i = 0
# while i < 3:
#     print(i)
#     i += 1

# for i in range(1, 5):
#     print(i * '*')

# strr=[1,2,3,10,35,33,22,25]
# for i in strr:
#     if i>=10:
#         print(True)
# print(i)

# for i in range(5):
#     if i == 3:
#         break
#     print(i)
    
# for i in range(5):
#     if i == 3:
        
#     print(i)

# x = [10, 20, 30]
# for item in x:
#     print(item)

# for i in range(2):
#     for j in range(2):
#         print(i, j)

# for i in range(5, 0, -1):
#     print(i)

# for i in range(1, 10, 3):
#     print(i)

# count = 0
# while count < 5:
#     print(count)
#     count += 2

# x = 0
# while x < 3:
#     x += 1
#     if x == 2:
#         continue
#     print(x)

# for i in range(3):
#     for j in range(2):
#         print(i + j ,end=)

# for i in range(3):
#     print('Loop', i)
# else:
#     print('Done')

# i = 0
# while i < 3:
#     print(i)
#     i += 1
# else:
#     print('Finished')

# for i in [0, 1, 2]:
#     if i:
#         print('Yes')
#     else:
#         print('No')

# for i in range(2):
#     for j in range(2):
#         if i == j:
#             print('Equal')

# for i in range(3):
#     pass
# print('Done')

# for i in range(2):
#     print(i)
#     break

# for i in range(5):
#     if i % 2 == 0:
#         print(i)

# x = [1, 2, 3]
# for i in x:
#     x.append(i)
#     if len(x) > 6:
#         break
# print(x)

for i in range(3):
    print(i)
    i += 1
