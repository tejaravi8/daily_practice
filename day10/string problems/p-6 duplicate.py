# Remove duplicate characters.

name="raviteja"
new=""
for i in name:
    if i not in new:
        new+=i
print(new)