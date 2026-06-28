#TASK 1
a=input("Enter the string: ")

#TASK 2
strlen=len(a)
print(f"The length of string {a} is {strlen}")

#TASK 3

upstr=a.upper()
lowstr=a.lower()
print(f"The upper case is {upstr} and lower case is {lowstr}")

#TASK 4
revstr=a[::-1]
print(revstr)

# revstr = "".join(reversed(a))
# print(revstr)

#TASK 5
if(a==revstr):
    print(f"The string {a} is palindrome!")
else:
    print(f"The string {a} is not palindrome!")
    
#task 6:
countV=0
countC=0
for ch in a:
    if(ch=="a" or ch=="i" or ch=="e" or ch=="o" or ch=="u"):
        countV+=1
    else:
        countC+=1
print(f"Number of vowels are {countV} and consonants are {countC}")