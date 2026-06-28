# Task 1 
marks = int(input("Enter your  marks: "))

# Task 2. 
if marks >= 40:
    print("you are Pass")
else:
    print("you are Fail")

# Task 3
if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 50:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"
print("your grade is :", grade)

# Task 4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a >= b )and (a >= c):
    largest = a
elif (b >= a) and (b >= c):
    largest = b
else:
    largest = c
print("Largest number is:", largest)

# Task 5
year = int(input("Enter a year: "))
if (year%400==0 or (year%4==0 and year%100!=0)):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")