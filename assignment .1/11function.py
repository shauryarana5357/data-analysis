#TASK 1
def nit():
    print("First intership @nit jalandhar")

nit()

#TASK 2
def display(name):
    print(f"Goog morning {name}")

display("shaurya")

#TASK 3
def com(a,b):
    if a>b:
        return a
    else:
        return b
print("The greater among 8 and 9 is",com(8,9))

#TASK 4
def sum(a,b):
    return a+b

print("The sum of 8 and 9 is",sum(8,9))

#TASK 5

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(f"The factorial of {n} is {fact}")
    
#TASK 6
def palindrome(n):
    temp=n
    rev=0
    while (temp>0):
        rev=rev*10+temp%10
        temp=temp//10

    if(n==rev):
        print(f"{n} is a palindrome")
    else:
        print(f"{n} is not a palindrome")
    
palindrome(267)
