#TASK 1
v=int(input("Enter the number to which you want to print:"))
i=1
while(i<=v):
    print(i,end=" ")
    i+=1
print("\n")


#TASK 2
a=int(input("Ennter the number of terms you want in fabonacci series:"))
i=0
x,y=0,1
while(i<a):
    print(x,end=" ")
    t=x
    x=y
    y=t+y
    i+=1
print("\n")
    
#TASK 3

p = int(input("Enter a number: "))
r = 0
temp = p

while temp > 0:
   
    r = r* 10 + temp % 10   
    temp = int(temp / 10)       #or can use temp//10

print(f"Original number: {p}")
print(f"Reversed number: {r}")

#TASK 4
C=int(input("Enter a number to check weather it is plaindrome or not:"))
rev= 0
temp2 = C

while temp2 > 0:
   
    rev = rev * 10 + temp2 % 10   
    temp2 = int(temp2 / 10)       #or can use temp//10

if(rev==C):
    print("It is a palindrome!")
else:
    print("It is not a plaindrome!")

#TASK=4
k=int(input("Enter whose factorial you want:"))
product=1
i=1
while(i<=k):
    product*=i
    i+=1
    
print(f"The factorial of {k} is {product}")


#TASH 5
h=int(input("Enter the number for digit sum:"))
digSum=0
temp3=h
while(temp3>0):
    digSum+=temp3%10
    temp3=temp3//10
    
print(f"The sum of digits of {h} is {digSum} ")

