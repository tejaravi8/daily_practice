# Create a List of Factorials
# Example: [1, 2, 3, 4] → [1, 2, 6, 24]

nums=[1,2,3,4]

factorials = []
for num in nums:
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    factorials.append(fact)

print("Factorials:", factorials)
