import random
class Bank:
    New_accounts=[]
    
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$            Well Come to Airtel Payments Bank           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    
#-----------------------------------------------        Create Acoount      -----------------------------------------------#
    def Create_account(self):
        
        new_account_holder={}
        
        name=input('Enter your name:')
        
        if name.isalpha():
            if name[0].isupper() :
                new_account_holder['Full Name']=name
            else:
                print("First letter should be in Capital..'(A-Z)")
        else:
            print('Enter Letters only')   
                    
            
        mobile=input('Enter your Mobile Number:')
        if len(mobile)==10:
            new_account_holder["Mobile_num"]=mobile
        else:
            print('Enter valid number')
            
        aadhar=input('Enter your Aadhar Number:')
        if len(aadhar)==12:
            new_account_holder["Aadhar_num"]=aadhar
        
        Account=random.randint(1000000000,9999999999)
        
        new_account_holder["Account_num"]=Account
        new_account_holder["IFSC Code"]="AIRP0000001"
        
        Bank.New_accounts.append(new_account_holder)
        print(Bank.New_accounts)
        
obj=Bank()
for x in range(1):
    obj.Create_account()