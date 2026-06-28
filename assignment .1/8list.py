#TASK 1
number=[10,20,30,40,50,60]
actnum=number[:]
print("The actual list:",number)

#TASK 2
number.append(70)
print("The list after append 70:",number)
number.insert(3,80)
print("The list after insert(3,80) :",number)


#TASK 3
number.pop()
print("The list after pop():",number)
number.pop(4)
print("The list after pop(4):",number)
number.remove(30)           # remove by value
del number[0]              # remove by index
print("After removing:", number)

#TASK 4
number.sort()
print("The list after sort():",number)

#TASK 5
number.reverse()
print("The list after reverse():",number)

#TASK 6
largest = max(number)
smallest = min(number)
print("Largest:", largest, "Smallest:", smallest)

#TASK 7

total=sum(number)
print("The sum of list member:", total)
print("The average of list member:", total/(len(number)))

#TASK 8
z=int(input("Enter the number whose occuance you want to cheack:"))
print(f"{z} appers in number {number.count(z)} times")

#TASK 9
print("After slicing",number[0:3])

#TASK 10
print("The list after all the operation become",number,"from",actnum)
