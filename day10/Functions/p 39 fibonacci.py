# Write a function to find nth Fibonacci number.

def fibonacci():
    a,b=0,1
    n=int(input("enter a number:"))
    for i in range(1,n+1):
        print(a)
        a,b=b,a+b
          
fibonacci()