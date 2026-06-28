#TASK 1
student = {"name": "Shaurya", "roll": 25, "marks": [85, 90, 78]}

#TASK 2
student["course"] = "B.Tech"
student.update({"Branch": "CSE(AI&ML)", "year": 1})   # update() adds multiple keys

#TASK 3
student["roll"] = 2510104065
student.update(roll=103)

#TASK 4
del student["year"]
removed = student.pop("year", None)


#TASK 5
print("Keys:", student.keys())

#TASK 6
print("Values:", student.values())

#TASK 7
key = "course"
if key in student:
    print(f"'{key}' found → {student[key]}")
else:
    print(f"'{key}' not found")

#TASK 8
avg = sum(student["marks"]) / len(student["marks"])
print("Average marks:", avg)

#TASK 9
for k in sorted(student.keys()):
    print(k, ":", student[k])

#TASK 10
print(f"Student {student['name']} (Roll {student['roll']}) has marks {student['marks']} with average {avg:.2f}")
