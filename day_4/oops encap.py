class Bank:
    
    def __init__(self):
        self.__pin=5528
        self.__bal=1521
        
    def check_bal(self,pin):
        if self.__pin == pin:
            print(f"your balance is {self.__bal}")
        else:
            print("Error!!  Entered wrong pin")
   
    def moneydeposit(self,pin,Depose):
        if self.__pin== pin:
            self.__bal+=Depose
            print(f"{Depose} got deposited")
            print(f"Successfully add, available balance is {self.__bal}")
        else:
            print("Error!!  Entered wrong pin")   
            
    def withdraw(self,pin,wAmount):
        if self.__pin==pin:
            self.__bal-= wAmount
            print(f"{wAmount} got debited")  
            print(f"remaining balance is {self.__bal}")
        else:
            print("Error!!  Entered wrong pin")   
    
pablo=Bank()
upi_pin=int(input("enter your pin:"))
# pablo.check_bal(upi_pin)
Depose=int(input("Enter Deposit amount:"))
pablo.moneydeposit(upi_pin,Depose)
# Withamt=int(input("enter withdraw amount:"))
# pablo.withdraw(upi_pin,Withamt)