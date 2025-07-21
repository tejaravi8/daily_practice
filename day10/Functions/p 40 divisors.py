# Create a function that returns list of all divisors of a number.

def divisors():
    n=int(input("Enter a number:"))
    l=[i for i in range(1,n+1) if n%i==0]
    return print(l)
divisors()