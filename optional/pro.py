import random

class student:
    students=[]

    def __init__(self,name,roll,marks):
        
        student={}
        student['Name'] = name
        student['Roll'] = roll
        student['Marks'] = marks
        student["Total"]= self.Total=0
        student["Avarage"]=self.avarage=0
        student["Grade"]=""
        
    def calculation(self):
        self.Total = sum(self.marks.values())
        self.avarage = self.Total / len(self.marks)
        
        if 100>= self.avarage >=90:
            self.grade="A"
        elif 89>= self.avarage >=75:
            self.grade="B"
        elif 74 >= self.avarage >= 60:
            self.grade="C"
        elif 59 >= self.avarage >= 35:
            self.grade="D"
        else:
            self.grade="Fail"
            
    def display(self):
        print(student['Name'])
        print(student['Roll'])
        print(student['Marks'])
        print(student["Total"])
        print(student["Avarage"])
        
s1=student()


s1.calculation()
s1.display()
    
# #     Name   : Ravi  
# # RollNo : 101  
# # Marks  : {'Math': 90, 'Science': 85, 'English': 80}  
# # Total  : 255  
# # Avg    : 85.0  
# # Grade  : A

# # Topper: Ravi (255 marks)

    
#     def __init__(self,name,roll,branch):
#         self.name=input("enter student name:")
#         self.year="IV year"
#         self.roll=random.randint(2182951001,2182951010)
#         self.branch=input("enter your branch name:")
        
#     def subjects(self):
#         english=int(input("enter marks:"))
#         python=int(input("enter marks:"))
#         frontend=int(input("enter marks:"))
#         digital_electr=int(input("enter marks:"))
        
#         total=english+python+frontend+digital_electr
        
        
#     def display(self):
        
#         print(f"name: {self.name} year: {self.year}
              
#               f"branch : {self.branch\n} "
              
#               f"roll : {self.roll}"
#               )
        
# obj=student()
# obj.student_details()
# obj.display()

        