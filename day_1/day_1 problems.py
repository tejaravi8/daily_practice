# Write a program to find the sum and average of all elements in a list.
# Example: [10, 20, 30, 40] → Sum: 100, Average: 25.0

numbers=[10,20,30,40]
sum=0
avg=0
for i in numbers:
    sum+=i
    avg=sum/len(numbers)
print(f"sum:{sum},average: {avg}")