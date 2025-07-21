# ✅ String and Basic Operations

# 1.Reverse a string.

name="Raviteja"
rev=""
for i in name:
    rev=i+rev
print(rev)

# method-2

for i in range(0,len(name)):
    rev=name[i]+rev
print(rev)

# method-3

print(name[::-1])