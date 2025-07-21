names=["teja","chandu","ganesh","drusyanth","ganesh","charan","tarun","hemanth"]

freq={}
for i in names:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
print(freq)