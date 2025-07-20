# Check if two strings are anagrams.(   "listen" --> "silent"   )

a, b = "listen", "silent"
print(sorted(a) == sorted(b))


# n=sorted(a)           #['a', 'e', 'j', 't']
# m=sorted(b)           #['a', 'e', 'j', 't']
# print(n==m)           True
