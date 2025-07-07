# Given a list, move all zeros to the end while keeping the order of non-zero elements.
# Example: [0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]

nums = [0, 1, 0, 3, 12]

result = []

# Add non-zero elements first
for num in nums:
    if num != 0:
        result.append(num)

# Count zeros
zeros = nums.count(0)

# Add zeros at the end
result.extend([0] * zeros)

print("Zeros moved:", result)
