# Swap keys and values in dict.

TCS={"pablo":33,
      "anya":25,
      "teja":10,
      "charan":43}

Tcs={}
for i,j in TCS.items():
    Tcs[j]=i 
print(Tcs)
