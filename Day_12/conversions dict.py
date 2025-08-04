students = {
    "Ravi": {"Math": 80, "English": 70, "Science": 60},
    "Teja": {"Math": 90, "English": 85, "Science": 75},
    "Ajay": {"Math": 60, "English": 75, "Science": 80}
}

# max=""
# count=0
# for k,i in students.items():
#     sum=0
#     for j in i.values():
#         sum+=j
#     if sum>count:
#         count=sum
#         max=k
# print(max)

# max=""
# count=0
# for i,k in students.items():
#     maximum=sum(k.values())
#     if maximum>count:
#         count=maximum
#         max=i
# print(max)

# 🧠 Problem 2: Subject-Wise Average Marks
# 🎯 Goal:
# You're given a nested dictionary where keys are student names and values are dictionaries of subject marks.

# ✅ Your Task:
# Calculate and print the average marks scored in each subject across all students.

students = {
    "Ravi": {"Math": 80, "English": 70, "Science": 60},
    "Teja": {"Math": 90, "English": 85, "Science": 75},
    "Ajay": {"Math": 60, "English": 75, "Science": 80}
}

# Step 1: Create a dictionary to store total marks per subject
subject_totals = {"Math": 0, "English": 0, "Science": 0}
num_students = len(students)

for i,j in students.items():
    for t,y in j.values():
        