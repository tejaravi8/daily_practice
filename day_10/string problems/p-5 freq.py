# Find frequency of characters in a string.

name="abcabc"
freq={}
for i in name:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1      
print(freq)

