# fruits=["mango","apple","banana","orange","watermelon"]

# create and access

# print(fruits[0])
# print(fruits[len(fruits)-1])

# for fruit in fruits:
#     print(fruit)

# update element in a list

# fruits=["mango","apple","banana","orange","watermelon"]
# fruits[1]="kiwi"

# print(fruits)

# add element
# fruits=["mango","apple","banana","orange","watermelon"]

# # Add 'grape' at index 2.
# # Add 'pineapple' at the end of the list.
# # Print the list.

# fruits.insert(2,'grape')         #['mango', 'apple', 'grape', 'banana', 'orange', 'watermelon']

# fruits.append("pineapple")        #['mango', 'apple', 'grape', 'banana', 'orange', 'watermelon', 'pineapple']
# print(fruits)  


# Delete Element

# Remove 'kiwi' from the list.  
# Delete the last element using pop().
# Print the final list.

# fruits=['mango', 'apple', 'grape', 'banana', 'orange', 'watermelon', 'pineapple']

# fruits.remove('mango')     #['apple', 'grape', 'banana', 'orange', 'watermelon', 'pineapple']
# # a=fruits.pop(2)          #['apple', 'grape', 'orange', 'watermelon', 'pineapple']

# print(fruits)
# print(a)

# # Slicing
# # Print the first 3 fruits.
# # Print fruits in reverse order (using slicing).

# fruits=["apple","banana","pineapple","orange","watermelon"]

# print(fruits[0:4:])
# print(fruits[::-1])

# Copy a List

#  Make a copy of the list using slicing.
# Change the first element in the copy to 'papaya'.
# Show that the original list did not change.

# fruits=["apple","banana","pineapple","orange","watermelon"]

# copy=fruits[0:4]                  # ['apple', 'banana', 'pineapple', 'orange']
# copy[0]='papaya'

# print(copy)                # ['papaya', 'banana', 'pineapple', 'orange']
# print(fruits)               # ["apple","banana","pineapple","orange","watermelon"]

# clear the list

# fruits.clear()
# print(fruits)

fruits=['mango', 'apple', 'grape', 'banana', 'orange', 'watermelon', 'pineapple']

print(fruits[0]) 
fruits[0]='papaya'
print(fruits[0],'updated')

fruits.append('dragon fruit')
print(fruits,'added')
fruits.remove('papaya')
print(fruits,'remove')

copy= fruits[-1:-4:-1]
print(copy,'copy')

copy.clear()
print(copy,'cleared list')
