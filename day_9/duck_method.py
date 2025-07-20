# class Duck:
#     def quack(self):
#         print("Quack Quack!")

# class Person:
#     def quack(self):
#         print("I can mimic a duck!")

# def make_it_quack(duck_like):
#     duck_like.quack()  # No type check

# d = Duck()
# p = Person()

# make_it_quack(d)  # Quack Quack!
# make_it_quack(p)  # I can mimic a duck!

# class pablo:
#     def age(self):
#         print('age of pablo is 21')
        
# class anya:
#     def age(self):
#         print('age of anya is 21')
        
# def get_age(data):
#     data.age()
    
# p=pablo()
# get_age(p)

# a=anya()
# get_age(a)

class Student:
    count = 0  # class variable

    def __init__(self, name):
        self.name = name
        Student.count += 1

    @classmethod
    def get_count(cls):  # Class method
        return 

# Usage
s1 = Student("Teja")
s2 = Student("Ravi")
print(Student.get_count())  # Output: 2
