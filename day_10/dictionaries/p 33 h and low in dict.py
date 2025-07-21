# Find highest and lowest value in dict.

TCS={"pablo":33,
      "anya":25,
      "teja":10,
      "charan":43}

max=0
min=float('inf')
for i in TCS.values():
    if max<=i:
        max=i
for i in TCS.values():
    if min>i:
        min=i
print(max,min)