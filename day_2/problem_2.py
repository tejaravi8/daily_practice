# # Count how many times each number appears in a list.
# # Example: [1, 2, 2, 3, 1, 4, 2] → {1: 2, 2: 3, 3: 1, 4: 1}
# # (Hint: Use a dict.)

numbers = [1, 2, 2, 3, 1, 4, 2]

freq = {}  

for num in numbers:
    if num not in freq:
        freq[num] = 0
    else:
        freq[num] += 1

print("Frequency:", freq)


