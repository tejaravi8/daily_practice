#======================================== INHERITENCE USING CONSTRUCTOR ========================================#
# class Animal:
#     def __init__(self):
#         print("discuss abount how animal sound")
        
#     def movement(self,m):
#         self.m=m
#         print(f"animals are dont {self.m} like humans")
        
# class dog(Animal):
#     def speak(self):
#         # super().__init__()
#         print("dog barks")
        
# obj=dog()                                   # Automatically runs the Constructor
# # obj.speak()

#======================================== SINGLE INHERITENCE ========================================#

# class Animal:
#     def speak(self):
#         print("discuss abount how animal sound")
        
#     def movement(self,m):
#         self.m=m
#         print(f"animals are dont {self.m} like humans")
        
# class dog(Animal):
#     def speak(self):
#         super().speak()                             #super().__init__()   incase of constructor
#         print("dog barks")
        
# obj=dog()
# obj.speak()

#======================================== MULTIPLE INHERITENCE ========================================#

# class Pablo:
#     def char(self):
#         print("Good boy")

# class Anya:
#     def char2(self):
#         print("Intelligent boy")
        
# class Teja(Pablo,Anya):
#     def char(self):
#         super().char()           # Here " Super() " indicates Pablo(parent), because we assigned first on Class Teja("Pablo",Anya)
#         print("silent boy")

# obj=Teja()
# obj.char()
# obj.char2()                     # calling method directly using object


#======================================== MULTILEVEL INHERITENCE ========================================#

# class Grandparent:
#     def grandfather(self):
#         print("Hi , im your Grand parent ")
        
# class Parent(Grandparent):
#     def father(self):
#         super().grandfather()                                         # no need super().__init__() in case of constructor
#         print("hi, im youR parent")
        
# class son(Parent):
#     def teja(self):
#         super().father()
#         print("hi, parent and grandparent")

# obj=son()
# obj.teja()
# # obj.grandfather()

#======================================== HIERARCHICAL INHERITENCE ========================================#

# # when multiple child classes inherit from a single parent class , it is called hierarchical inheritence

# class parent:
#     def method(self):
#         print("parent")
        
# class child1(parent):
#     def method(self):
#         print("child 1")
        
# class child2(parent):
#     def method(self):
#         print("child 2")
        
# class child3(parent):
#     def method(self):
#         print("child 3")
        
# obj=child1()
# obj.method()       #calling method init
# obj1=child2()
# obj2=child3()   

#======================================== HIERARCHICAL INHERITENCE ========================================#
# class Grandparent:
#     def method(self):
#         print("grand parent class")
        
# class Parent(Grandparent):
#     def method2(self):
#         print("Parent class")
        
# class Parent2:
#     def method3(self):
#         print("parent2 class")
        
# class Child(Parent,Parent2):
#     def method4(self):
#         print("child Class")
        
# obj=Child()
# obj.method4()

a=[1,2,3,4,5,6,7,8,9]

for i in range(1,3):
    a.pop(i)
        
print(a)