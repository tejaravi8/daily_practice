# Create a list of the first 10 natural numbers.

# num=10
# my_list=[]
# for i in range(1,num+1):
#     my_list.append(i)
# print(my_list)

# Print the last 3 elements of a list.

# my_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for i in range(len(my_list)-3,len(my_list)):
#     print(my_list[i])

# result=my_list[-3:]
# print(result)

# Replace the middle element in a list with the number 100.

# my_list=[1, 2, 3, 4, 5, 6, 7, 8,9]

# if len(my_list)%2 != 0:
#     middle=len(my_list)//2
#     a=my_list[middle]
    
# else:
#     middle=len(my_list)//2
#     my_list[middle]='b'
    
# print(my_list)
    
# p='my name is hemanth'
# a=''
# # p[-2]
# for i in p:
#     if i !=' ':
#         a+=i

# n=a[-2:len(a):]+a[-10::-1]+a[6:8]+a[-7:-2:]
# print(n)

# print(f"{a[-2:len(a):]}gehjjfjdnf {a[-10::-1]} {a[6:8]} {a[-7:-2:]}")

# th emanym is heman

# a='teja'
# b=a[-2::-1]
# print(b)

# Delete the second and third items in a list.
# my_list=[1, 2, 3, 4, 5, 6, 7, 8,9]

# for i in my_list:
#     if i==my_list[1] :
#         my_list.remove(i)
        
# print(my_list)

# Check if 15 is in the list [10, 20, 15, 30]
# my=[10,20,15,30]

# for i in my:
#     if i==15:
#         print('yes it is found here')


# Create a list from user input of 5 numbers.

# listt=[]
# for i in range(1,6):
#     a=input('enter number:')
#     listt.append(a)

# print(listt)

# Find the sum of all numbers in a list.

# my=[10,20,15,30]
# sum=0
# for i in my:
#     sum+=i
# print(sum)

# Count how many times 0 appears in [1, 0, 2, 0, 3, 0]

# my=[1, 0, 2, 0, 3, 0]
# count=0

# for item in my:
#     if item==0:
#         count+=1
# print(count)

# Find the max and min number in a list.

# my=[1, 0, 2, 0, 3, 0]
# max_num=0
# min_num=float('inf')

# for i in my:
#     if i>max_num:
#         max_num=i
# print(max_num,'max')
# for i in my:
#     if i<min_num:
#         min_num=i
# print(min_num,'min')

# Reverse a list without using .reverse().
# my=[1, 0, 2, 0, 3, 0]

# rev=[]
# for i in range(-1,-7,-1):
#     rev.append(my[i])
    
# print(rev)

# Print each index and value using a loop.

# my=[1, 'a', 's', 'e', 3, 0]
# for i in range(0,len(my)):
#     print(i,my[i])

# Find the average of numbers in a list.
# my=[1,2,3,4,5,6,7,8]
# sum=0
# for i in my:
#     sum+=i
    
# avg=sum/len(my)   
# print(avg)

# Print items in reverse order using a loop.
# my=[1, 'a', 's', 'e', 3, 0]
# for i in range(len(my)-1,-1,-1):
#     print(my[i])
    
# my.reverse()
# print(my)

# Print only those elements whose index is even.
# my=[1, 'a', 's', 'e', 3, 0]
# for i in range(0,len(my)):
#     if i%2==0:
#         print(my[i])

# 16.Loop through a list and print the square of each item.

# my=[1,2,3,4,5,6,7,8]
# for i in my:
#     print(i**2)
    
# 17.Create a new list of only positive numbers.
# pos_list=[]
# for i in range(1,101):
#     pos_list.append(i)
    
# print(pos_list)

# 18.Replace all negative numbers in a list with 0.
# my=[1,2,-3,4,-5,6,-7,8]

# for i in range(0,len(my)):
#     if my[i]<0:
#         my[i]=0
        
# print(my)

# 🔧 List Methods (19–27)
# Use .append() to build a list from an empty list.

# my=[]
# for i in range(1,11):
#     my.append(i)
# print(my)
#------------------------------------------------
# Use .insert() to add 99 at index 2.
# old=[0,1,3,4,5,6,7,8,9,10]
# old.insert(2,99)
# print(old)
#--------------------------------------------------
# Use .remove() to remove first occurrence of 3.
# old=[0,1,3,4,3,6,7,8,9,10]

# old.remove(3)
# print(old)
#-----------------------------------------------
# # Use .pop() to remove the last element.
# old=[0,1,3,4,3,6,7,8,9,10]

# old.pop(1)   #by index
# print(old)
#------------------------------------------------------
# Use .count() to count how many times 1 appears.
# old=[0,1,3,1,1,6,7,8,1,10]
# a=old.count(1)
# print(a)
#------------------------------------------------------
# Sort a list in descending order.
# old=[0,1,3,1,1,6,7,8,1,10]
# for i in range(0,len(old)):
#     for j in range(i+1,len(old)):
#         if old[i]>old[j]:
#             old[i],old[j]=old[j],old[i]
            
# print(old)
#----------------------------------------------------
# Clear all elements from a list.
# old=[0,1,3,1,1,6,7,8,1,10]

# old.clear()
# print(old)
        
# for i in old:
#     old.remove(i)
#     print(old)
# print(old,'last')
#---------------------------------------------------
# Find the index of number 5 in a list.

# old=[0,1,3,5,7,8,1,10]

# for i in old:
#     if i==5:
#         print(old.index(i))
#-------------------------------------------------
# Extend a list with another list of values.
# a=[0,1,3,5,7,8,1,10]
# a2=[4,6,990,1,2,8]

# a.extend(a2)
# print(a)
#--------------------------------------------
# 🎯Filtering + Searching (28–35)
# Print all elements > 25 from the list.
# list_1=[1,2,3,34,45,67,25,99]
# for i in list_1:
#     if i>25:
#         print(i)
# -----------------------------------------
# Check if a list is a palindrome.

# lis=[1,2,3,2,1]
# lis2=[]
# for i in range(len(lis)-1,-1,-1):
#     lis2.append(lis[i])
    
# if lis2==lis:
#         print('palindrome')
# else:
#         print('not a palindrome')
# ---------
# if lis[-1::-1]==lis:
#     print('palindrome') 
# else:
#     print('Not a palindrome')

#-------------------------------------------------
# Return a new list with only even numbers.
# listt=[1,2,3,4,5,6,7,8,9,10]
# returnn=[]

# def even():
#     for i in listt:
#         if i%2==0:
#             returnn.append(i)    
#     return print(returnn)
# even()
#---------------------------------------------------
# Filter elements divisible by 3.
# listt=[1,2,3,4,5,6,7,8,9,10]
# for i in listt:
#     if i%3==0:
#         print(i)
#---------------------------------------------------
# Find all numbers greater than the average. 

# listt=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in listt:
#     sum+=i
# avg=sum/len(listt)
# for j in listt:
#     if j>avg:
#         print(j)
#---------------------------------------------------
# Remove all zeroes from a list.
#listt=[1,2,0,4,0,1,1,0,3]

# for i in listt:
#     if i==0:
#         listt.remove(i)
        
# print(listt)
#---------------------------------------------------
# Return True if the list has duplicates
# listt=[1,2,0,4,0,1,1,0,3]
# lis=[]
# for i in listt:
#     if i not in lis:
#         lis.append(i)
#     else:
#         print('True')
#         break
#---------------------------------------------------
# Return list of elements that appear more than once.

#---------------------------------------------------
# Find all pairs in a list that sum to 10.

# listt=[1,2,3,4,5,6,7,8,9,10]

# for i in listt:
#     for j in listt:
#         if i+j==10:
#             print((i,j))

# Find all unique pairs that sum to a given target.
# listt=[1,2,3,4,5,6,7,8,9,10]

# for i in range(0,len(listt)):
#     for j in range(i+1,len(listt)):
#         if listt[i]+listt[j]==10:
#             print((listt[i],listt[j]))

#---------------------------------------------------
# # Print all pairs (i, j) where i != j.
# listt=[1,2,3,4,5,6,7,8,9,10]

# for i in range(0,len(listt)):
#     for j in range(i+1,len(listt)):
#         if listt[j]!=listt[i]:
#             print((listt[i],listt[j]))

# From two lists, print all combinations (cross product).   #question not understand

# Check if any 2 numbers in list add to 100.   #41

# Count number of such valid pairs in a list.   #42

#---------------------------------------------------
# Generate a list of squares using list comprehension.

# a=[i**3 for i in range(1,11)]
# print(a)
#---------------------------------------------------
# Create a list of even numbers from 1 to 50.
#---------------------------------------------------
# Create a list of words with length > 3 from a sentence.

# lis=input('enter here:')
# new_lis=lis.split()
# nn=[]
# for i in new_lis:
#     if len(i)>3:
#         nn.append(i)
# print(nn)
#---------------------------------------------------
# Extract only vowels from a given string using list comprehension.

# name='teja'
# vowels=[a for a in name if a in 'aeiou']
# print(vowels)

#---------------------------------------------------

# Create a list of numbers not divisible by 5 from 1 to 30.

# multi_5=[i for i in range(1,31) if i%5==0]
# print(multi_5)

#---------------------------------------------------
# Check if list is increasing or decreasing.


#---------------------------------------------------
# # Rotate a list to the left by 2 steps.
listt=[1,2,3,4,5,6,7,8,9,10]
k=2
new_list=listt[-k:]+listt[:-k]
print(new_list)


#---------------------------------------------------
# Merge two sorted lists into one sorted list.

# listt=[1,2,3,4,5,6,7,8,9,10]

# a=listt[2:6]
# b=listt[-1:-6:-1]
# c=a+b
# print(c)
#--------------------The end-------------------------------


#  #============================           QUESTIONS      ==========================================================
# ✅ Basic List Operations (1–10)

# 1.Create a list of the first 10 natural numbers.
# 2.Print the last 3 elements of a list.
# 3.Replace the middle element in a list with the number 100.
# 4.Delete the second and third items in a list.
# 5.Check if 15 is in the list [10, 20, 15, 30].
# 6.Create a list from user input of 5 numbers.
# 7.Find the sum of all numbers in a list.
# 8.Count how many times 0 appears in [1, 0, 2, 0, 3, 0].
# 9.Find the max and min number in a list.
# 10.Reverse a list without using .reverse().

# 🔁 Looping Through Lists (11–18)

# 11.Print all odd numbers from a list.
# 12.Print each index and value using a loop.
# 13.Find the average of numbers in a list.
# 14.Print items in reverse order using a loop.
# 15.Print only those elements whose index is even.
# 16.Loop through a list and print the square of each item.
# 17.Create a new list of only positive numbers.
# 18.Replace all negative numbers in a list with 0.

# 🔧 List Methods (19–27)

# 19.Use .append() to build a list from an empty list.
# 20.Use .insert() to add 99 at index 2.
# 21.Use .remove() to remove first occurrence of 3.
# 22.Use .pop() to remove the last element.
# 23.Use .count() to count how many times 1 appears.
# 24.Sort a list in descending order.
# 25.Clear all elements from a list.
# 26.Find the index of number 5 in a list.
# 27.Extend a list with another list of values.

# 🎯 Filtering + Searching (28–35)

# 28.Print all elements > 25 from the list.
# 29.Check if a list is a palindrome.
# 30.Return a new list with only even numbers.
# 31.Filter elements divisible by 3.
# 32.Find all numbers greater than the average.
# 33.Remove all zeroes from a list.
# 34.Return True if the list has duplicates.
# 35.Return list of elements that appear more than once.

# 🎲 Pairing, Combinations (36–42)

# 36.Find all pairs in a list that sum to 10.
# 37.Find all unique pairs that sum to a given target.
# 38.Print all pairs (i, j) where i != j.
# 39.Print all combinations of 2 different elements.
# 40.From two lists, print all combinations (cross product).
# 41.Check if any 2 numbers in list add to 100.
# 42.Count number of such valid pairs in a list.

# 🧮 List Comprehension (43–47)

# 43.Generate a list of squares using list comprehension.
# 44.Create a list of even numbers from 1 to 50.
# 45.Create a list of words with length > 3 from a sentence.
# 46.Extract only vowels from a given string using list comprehension.
# 47.Create a list of numbers not divisible by 5 from 1 to 30.

# 🧩 Pattern-Based Problems (48–50)

# 48.Check if list is increasing or decreasing.
# 49.Rotate a list to the left by 2 steps.
# 50.Merge two sorted lists into one sorted list.

# # ========================     answers   =========================

# ✅ Basic List Operations (1–10)

# 1.  numbers = list(range(1, 11))
# 2.  print(my_list[-3:])
# 3.  my_list[len(my_list)//2] = 100
# 4.  del my_list[1:3]
# 5.  print(15 in [10, 20, 15, 30])
# 6.  user_input = [int(input()) for _ in range(5)]
# 7.  print(sum(my_list))
# 8.  print([1, 0, 2, 0, 3, 0].count(0))
# 9.  print(max(my_list), min(my_list))
# 10. reversed_list = my_list[::-1]

# 🔁 Looping Through Lists (11–18)

# 11. print([x for x in my_list if x % 2 != 0])
# 12. for idx, val in enumerate(my_list): print(idx, val)
# 13. avg = sum(my_list)/len(my_list)
# 14. for x in reversed(my_list): print(x)
# 15. print([my_list[i] for i in range(0, len(my_list), 2)])
# 16. for x in my_list: print(x**2)
# 17. positives = [x for x in my_list if x > 0]
# 18. my_list = [x if x >= 0 else 0 for x in my_list]

# # 🔧 List Methods (19–27)

# 19. result = []; result.append(10)
# 20. my_list.insert(2, 99)
# 21. my_list.remove(3)
# 22. my_list.pop()
# 23. my_list.count(1)
# 24. my_list.sort(reverse=True)
# 25. my_list.clear()
# 26. my_list.index(5)
# 27. my_list.extend([6, 7, 8])

# # 🎯 Filtering + Searching (28–35)

# 28. [x for x in my_list if x > 25]
# 29. my_list == my_list[::-1]
# 30. [x for x in my_list if x % 2 == 0]
# 31. [x for x in my_list if x % 3 == 0]
# 32. avg = sum(my_list)/len(my_list); [x for x in my_list if x > avg]
# 33. [x for x in my_list if x != 0]
# 34. len(my_list) != len(set(my_list))
# 35. [x for x in set(my_list) if my_list.count(x) > 1]

# # 🎲 Pairing, Combinations (36–42)

# 36. [(x, y) for i, x in enumerate(my_list) for y in my_list[i+1:] if x + y == 10]
# 37. seen = set(); pairs = set()
#     for num in my_list:
#         if 10 - num in seen:
#             pairs.add(tuple(sorted((num, 10-num))))
#         seen.add(num)
# 38. [(i, j) for i in my_list for j in my_list if i != j]
# 39. [(i, j) for idx, i in enumerate(my_list) for j in my_list[idx+1:]]
# 40. [(i, j) for i in list1 for j in list2]
# 41. target = 100; seen = set(); found = False
#     for num in my_list:
#         if target - num in seen:
#             found = True
#             break
#         seen.add(num)
# 42. count = 0
#     for i in range(len(my_list)):
#         for j in range(i+1, len(my_list)):
#             if my_list[i] + my_list[j] == 10:
#                 count += 1

# # 🧮 List Comprehension (43–47)

# 43. squares = [x**2 for x in range(1, 11)]
# 44. evens = [x for x in range(1, 51) if x % 2 == 0]
# 45. [word for word in sentence.split() if len(word) > 3]
# 46. [ch for ch in string if ch.lower() in 'aeiou']
# 47. [x for x in range(1, 31) if x % 5 != 0]

# # 🧩 Pattern-Based Problems (48–50)

# 48. is_increasing = all(my_list[i] <= my_list[i+1] for i in range(len(my_list)-1))
#     is_decreasing = all(my_list[i] >= my_list[i+1] for i in range(len(my_list)-1))
# 49. rotated = my_list[2:] + my_list[:2]
# 50. merged = sorted(list1 + list2)