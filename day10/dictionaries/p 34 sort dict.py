# Sort a dictionary by values.

TCS={"pablo":33,
      "anya":25,
      "teja":10,
      "charan":43}
new={}
min=float("inf")
for j,i in range(4).values():
    if min>i:
        new[j]=i
        
print(new)
