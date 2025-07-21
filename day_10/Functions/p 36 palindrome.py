# Write a function to check palindrome.

def palindrome():
    name="madam"
    rev=name[::-1]
    if name==rev:
        print("palindrome")
    else:
        print("Not a palindrome")
palindrome()