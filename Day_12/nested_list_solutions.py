# 1. Flatten a deeply nested list
from collections.abc import Iterable

def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([[1, 2, [3, 4]], 5, [6, [7, 8]]]))

# 2. Maximum Sublist Sum
def max_sum_sublist(lst):
    return max(lst, key=lambda x: sum(x))

print(max_sum_sublist([[2, 3], [10, -2, 1], [4, 5, 6]]))

# 3. Rotate Matrix 90 degrees Clockwise
def rotate_matrix(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# 4. Count Even Numbers
def count_evens(nested):
    return sum(num % 2 == 0 for sub in nested for num in sub)

print(count_evens([[1, 2, 3], [4, 6, 7], [8]]))

# 5. Replace Target Number with -1
def replace_number(lst, target):
    return [[-1 if num == target else num for num in sub] for sub in lst]

print(replace_number([[1, 2, 3], [4, 2, 5]], 2))

# 6. Sort by Second Element
def sort_by_second(lst):
    return sorted(lst, key=lambda x: x[1])

print(sort_by_second([[1, 4], [3, 1], [5, 2]]))

# 7. Transpose Matrix
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

print(transpose([[1, 2, 3], [4, 5, 6]]))

# 8. Subject-wise Averages
def subject_averages(data):
    num_subjects = len(data[0])
    subject_sums = [0] * num_subjects
    for student in data:
        for i in range(num_subjects):
            subject_sums[i] += student[i]
    return [round(total / len(data), 2) for total in subject_sums]

print(subject_averages([[80, 70, 60], [90, 85, 75], [60, 75, 80]]))

# 9. Check Structural Equality
def same_structure(lst1, lst2):
    if isinstance(lst1, list) and isinstance(lst2, list):
        if len(lst1) != len(lst2): return False
        return all(same_structure(x, y) for x, y in zip(lst1, lst2))
    return not isinstance(lst1, list) and not isinstance(lst2, list)

print(same_structure([[1, 2], [3, 4]], [["a", "b"], ["c", "d"]]))

# 10. Multiplication Table
def multiplication_table():
    return [[(i+1)*(j+1) for j in range(10)] for i in range(10)]

print(multiplication_table())
