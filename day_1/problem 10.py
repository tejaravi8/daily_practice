# Given a list, split it into two lists: one with even numbers, one with odd numbers.
# Example: [10, 11, 12, 13] → Even: [10, 12], Odd: [11, 13]

numbers=[10,11,12,13]
even=[]
odd=[]

for i in numbers:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print('Even:',even)
print('Odd:',odd)