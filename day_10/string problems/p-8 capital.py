# Capitalize first letter of each word.

name="raviteja"
new=""
for i in range(0,len(name)):
    if i==0:
        new+=name[i].upper()
    else:
        new+=name[i]
print(new)

# for i in name:
#     if i==name[0]:
#         new+=i.upper()
#     else:
#         new+=i
# print(new)