# class student:
#     def __init__(self,name,roll):
#         self.name=name
#         self.roll=roll
# s1=student('teja',10)
# print('hi',s1.name,'we call you by your roll number',s1.roll)


# class hostel:
#     def __init__(self,name,bed_num):
#         self.name=name
#         self.bed=bed_num
# name=hostel('pablo',1)
# print('hello',name.name,'this is your bed no',name.bed)

class rack:
    def __init__(self,rack_num,name):
        self.num=rack_num
        self.name=name
    
    def room(self,bed):
        self.bednum=bed
    
    
 
name=rack(1,'annayya')
name.room(1)


# print(name.bednum)
# print(name.num,name.name)