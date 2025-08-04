# # a=14     #1 1 1 0
# # b=12     #1 1 0 0
# # # print(b&a)    #multiply


# # # print(a | b)   # addition

# # # print(~b)   # -1(b+1)
# # #             # -1(-12+1)
            
# # print(a << b)   # 
# #               # 1 1 0 0 1 1 1 0

# a=10
# b=20
# c=30
# d=40

# result= a<b<c<d
# print(result)      

class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks  # marks is a dict: {'Math': 80, 'Science': 90, 'English': 75}
        self.total = 0
        self.average = 0
        self.grade = ''

    def calculate_result(self):
        self.total = sum(self.marks.values())
        self.average = self.total / len(self.marks)

        if self.average >= 90:
            self.grade = 'A+'
        elif self.average >= 75:
            self.grade = 'A'
        elif self.average >= 60:
            self.grade = 'B'
        elif self.average >= 40:
            self.grade = 'C'
        else:
            self.grade = 'F'

    def display(self):
        print(f"\nName   : {self.name}")
        print(f"RollNo : {self.roll_no}")
        print(f"Marks  : {self.marks}")
        print(f"Total  : {self.total}")
        print(f"Average: {round(self.average, 2)}")
        print(f"Grade  : {self.grade}")


# 👇 Create multiple student objects
students = [
    Student("Ravi", 101, {'Math': 80, 'Science': 90, 'English': 75}),
    Student("Teja", 102, {'Math': 95, 'Science': 85, 'English': 78}),
    Student("Anil", 103, {'Math': 65, 'Science': 70, 'English': 60}),
]

# Calculate results and store topper info
for s in students:
    s.calculate_result()

# ✅ Display all results
print("📋 Student Report Cards")
for s in students:
    s.display()

# 🏆 Find the topper
topper = max(students, key=lambda s: s.total)
print(f"\n🏆 Topper: {topper.name} with {topper.total} marks")
