# Count vowels in a string.

name=input("enter your name:").lower()
vowels="aeiou"
count=0
for i in name:
    if i in vowels:
        count+=1
print(count)