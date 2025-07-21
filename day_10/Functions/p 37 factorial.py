# Write a function to return factorial.

def factorial():
    
    n=int(input("enter a number:"))
    factorial=1
    for i in range(1,n+1):
        factorial*=i
        
    return print(factorial)
factorial()