import random
class bank:
    HOLDER_DETAILS=[]
    print("=========WELLCOME TO SBI===========")
    def create_new_Account(self):
        # print("=========WELLCOME TO SBI===========")
        new_holder={}
    
        name=input('enter holder_name:-')
        if name.isalpha():
            while True:
                if name[0].isupper():
                    new_holder['holder_name']=name
                    break
                else:
                    print('First letter should be CAPITAL')

        mb=input('enter your mobile_no:- ')
        if len(mb)==10:
        
            new_holder['holder_mobile_no']=int(mb)
        else:
            print('only print valid num')

        aadhar=input('enter your aadhar_no:-- ')
        if len(aadhar)==12:
            new_holder['holder_aadhar_no']=int(aadhar)
        else:
            print('enter vaild aadhar_no')
        new_holder['IFSC']="IFSC220077"
        data=random.randint(100000000000,999999999999)
        new_holder['Account_no']=data
        n=input('enter type of account saving/zero:'.lower())
        if n=='saving':
            while True:
                n1=int(input('your Account saving so you have deposite 500 rupees:'))
                if n1>=500:
                    new_holder['balance']=n1
                    break
                else:
                    print('deposite  min 500 rupess')
        if n=='zero':
            while True:
                n2=int(input('your Account zero so you have deposite 100 rupees:'))
                if n2>=100:
                    new_holder['balance']=n2
                    break
                else:
                    print('deposite min 100 rupees')
        bank.HOLDER_DETAILS.append(new_holder)
        print(bank.HOLDER_DETAILS)
        
    def Deposite(self):
        n5=input('enter holder name:')
        n6=int(input('Account Number:'))
        n3=int(input('enter deposite money:'))
        for x in bank.HOLDER_DETAILS:
            if x['holder_name']==n5 and x['Account_no']==n6:
                data=x.get('balance')
                x['balance']=data+n3
            print(Bank.HOLDER_DETAILS)



obj=bank()
obj.create_new_Account()
# obj.Deposite()
