# class car:
#     def start(self):
#         return 'start'
# my=car()
# print(my.start())

# class car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
    
#     def details(self,name,classs):
#         self.classs=classs
#         self.name=name
#         # print(self.classs)
#         # print(self.name)
        
# my_car=car("BMW","M5")
# my_car.details('teja',12)
# print(my_car.brand)

# class institute:
#     name="10k coders"
#     def __init__(self):
#         self.free=30,000
#         self.course="python stack"
#     def student(self,Ts,Ap):
#         self.ts=Ts
#         self.ap=Ap
#     def batch(self,name,num):
#         self.name=name
#         self.num=num
        
# s1=institute()
# s1.batch("achievers","51R")
# print(s1.name)

#encapsulization

class Bank:
    print("==========={wellcome to Airtel Payments Bank}=======================")
    def __init__(self):
        self.__pin=41863
        self.__balance=4000
        
    def check_balance(self,pin):
        if self.__pin==pin:
            print(f"your balance is {self.__balance}")
            
    def deposit(self,pin):
        if self.__pin==pin:
            Dep_amt=int(input('Enter Deposit Amount:'))
            self.__balance += Dep_amt
            print(f"{Dep_amt} is deposit successfull,your available balance is {self.__balance}")
            
    def withdraw(self):
        pin=int(input("enter your pin:"))
        if self.__pin==pin:
            with_amt=int(input("enter withdraw amount:"))
            self.__balance -= with_amt
            print(f"{with_amt} is debited, your available balance is {self.__balance}")
            
user1=Bank()
while True:
    a=input("enter: 'withdraw' for withdraw , 'check' for check balance , 'cancel' for cancel transaction ")
    if a=="withdraw":
        user1.withdraw()  
        break
    elif a=="check":
        user1.check_balance(41863)
        break
    else:
        break
print("thanks for visiting")
# # user1.check_balance(41863)
# # user1.deposit(41863)
# user1.withdraw()
