# Find all pairs in a list that add up to a given target sum.
# Example: [1, 2, 3, 4, 5, 6] and target = 7 → Pairs: (1, 6), (2, 5), (3, 4)

# numlist=[1,2,3,4,5,6]
# target=7

nums = [1, 2, 3, 4, 5, 6]
target = 7

pairs = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            pairs.append((nums[i], nums[j]))

print("Pairs:", pairs)

