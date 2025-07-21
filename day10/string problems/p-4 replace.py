# Replace spaces with hyphens.

sentence=input("enter some data with spaces:").lower()
rev=""
for i in sentence:
    if i==" ":
        rev+="-"
    else:
        rev+=i
print(rev)