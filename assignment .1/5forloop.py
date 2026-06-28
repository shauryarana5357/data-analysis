# Task 1

print("Numbers from 1 to 100:")
for i in range(1, 101):
    print(i, end=" ")
print("\n")

# Task 2
print("Even numbers from 1 to 100:")
for i in range(2, 101, 2):
    print(i, end=" ")
print("\n")

# Task 3
print("Odd numbers from 1 to 100:")
for i in range(1, 101, 2):
    print(i, end=" ")
print("\n")

# Task 4
N = int(input("Enter N: "))
sum = 0
for i in range(1, N+1):
    sum += i
print(f"Sum of first {N} numbers = {sum}")

# Task 5
print("Squares of numbers from 1 to N:")
for i in range(1, N+1):
    print(f"{i}^2 = {i*i}")

# Task 6
num = int(input("Enter a number for factorial: "))
fact = 1
for i in range(1, num+1):
    fact *= i
print(f"Factorial of {num} = {fact}")

# Task 7
num = int(input("Enter a number to count digits: "))
count = 0
for digit in str(num):   
    count += 1
print(f"Number of digits in {num} ={count}")
