# 1. Flatten a deeply nested list (Simple Version)
def flatten(nested):
    result = []
    for item in nested:
        if type(item) == list:
            for sub_item in item:
                if type(sub_item) == list:
                    result.extend(sub_item)
                else:
                    result.append(sub_item)
        else:
            result.append(item)
    return result

print(flatten([[1, 2, [3, 4]], 5, [6, [7, 8]]]))

# 2. Maximum Sublist Sum
def max_sum_sublist(lst):
    max_list = lst[0]
    for sublist in lst:
        if sum(sublist) > sum(max_list):
            max_list = sublist
    return max_list

print(max_sum_sublist([[2, 3], [10, -2, 1], [4, 5, 6]]))

# 3. Rotate Matrix 90 degrees Clockwise
def rotate_matrix(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)-1, -1, -1):
            row.append(matrix[j][i])
        new_matrix.append(row)
    return new_matrix

print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

# 4. Count Even Numbers
def count_evens(nested):
    count = 0
    for sub in nested:
        for num in sub:
            if num % 2 == 0:
                count += 1
    return count

print(count_evens([[1, 2, 3], [4, 6, 7], [8]]))

# 5. Replace Target Number with -1
def replace_number(lst, target):
    result = []
    for sub in lst:
        new_sub = []
        for num in sub:
            if num == target:
                new_sub.append(-1)
            else:
                new_sub.append(num)
        result.append(new_sub)
    return result

print(replace_number([[1, 2, 3], [4, 2, 5]], 2))

# 6. Sort by Second Element
def sort_by_second(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i][1] > lst[j][1]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

print(sort_by_second([[1, 4], [3, 1], [5, 2]]))

# 7. Transpose Matrix
def transpose(matrix):
    result = []
    for i in range(len(matrix[0])):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        result.append(row)
    return result

print(transpose([[1, 2, 3], [4, 5, 6]]))

# 8. Subject-wise Averages
def subject_averages(data):
    math = 0
    eng = 0
    sci = 0
    for student in data:
        math += student[0]
        eng += student[1]
        sci += student[2]
    count = len(data)
    return [round(math/count, 2), round(eng/count, 2), round(sci/count, 2)]

print(subject_averages([[80, 70, 60], [90, 85, 75], [60, 75, 80]]))

# 9. Check Structural Equality
def same_structure(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(len(lst1)):
        if type(lst1[i]) == list and type(lst2[i]) == list:
            if len(lst1[i]) != len(lst2[i]):
                return False
        elif type(lst1[i]) != type(lst2[i]):
            return False
    return True

print(same_structure([[1, 2], [3, 4]], [["a", "b"], ["c", "d"]]))

# 10. Multiplication Table
def multiplication_table():
    table = []
    for i in range(1, 11):
        row = []
        for j in range(1, 11):
            row.append(i * j)
        table.append(row)
    return table

print(multiplication_table())
