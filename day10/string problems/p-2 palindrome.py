# Check if a string is a palindrome.

name="madam"            #sis   refer  mom  dad
reverse=""
for i in name:
    reverse=i+reverse
if reverse==name:
    print("it is a palindrome")
else:
    print("not a palindrome")

# same with slicing 

name="madam"  
reverse = name[::-1]
if reverse==name:
    print("it is a palindrome")
else:
    print("not a palindrome")