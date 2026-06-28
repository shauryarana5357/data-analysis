#TASK 1

def show(n):
    if(n==0):
        return
    print(n,end=" ")
    show(n-1)
    
show(9)
print("\n")
#TASK 2
def fact(n):
    if(n==0 or n==1):
        return 1
    return(n*fact(n-1))
print(fact(5))

#TASK 3

#TASK 1: Define a recursive function
def greet(n):
    if n == 0:   # base case
        return
    print("Hello")
    greet(n-1)   # recursive call

greet(3)

#TASK 2: Factorial recursively
def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    return n * factorial(n-1)

print("Factorial of 5:", factorial(5))

#TASK 3: 
def fibonacci(n):
    if n <= 1:   # base case
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci series (first 7 terms):", [fibonacci(i) for i in range(7)])

#TASK 4: 
def power(base, exp):
    if exp == 0:   # base case
        return 1
    return base * power(base, exp-1)

print("2^5 =", power(2, 5))

#TASK 5:
def reverse_string(s):
    if len(s) == 0:   # base case
        return s
    return reverse_string(s[1:]) + s[0]

print("Reverse of 'Shaurya':", reverse_string("Shaurya"))
    
    