student={
    1:{
    "geninfo":("shaurya","B.tech"),
    "marks":[98,97,90],
    "subject":{"maths","english","science"}
    }
}
student[2]={
    "geninfo":("shagun","BSc.nursing"),
    "marks":[88,87,99],
    "subject":{"physology","anatomy","physiology"}
}
def add_sturnt():
    a=int(input("Enter the roll number:"))
    b=(input("Enter the name:"))
    c=(input("Enter the course:"))
    d = input("Enter subjects (comma separated): ").split(",")
    e = list(map(int, input("Enter marks (comma separated): ").split(",")))
    student[a]={"geninfo":(b,c),"marks":e,"subject":d}
    print("Data sucessfully entered")


def display_students():
    x=int(input("Enter the roll number of the student:"))
    if x in student:
        print(student[x])
    else:
        print("No data found")


def ask():
    print("Enter 1 to add student")
    print("Enter 2 to display student")
    print("Enter 3 for class average")
    print("Enter 4 for individual student average")
    print("Enter 5 to to see topper info")
    print("Enter 6 to to see stats")
    ju=int(input("Enter command:"))
    if(ju==1):
        add_sturnt()
    elif(ju==2):
        display_students()
    elif(ju==3):
        avgc()
    elif(ju==4):
        avg()
    elif(ju==5):
        topper()
    elif(ju==6):
        stats()
        
        
def avgc():
    val=[m for data in student.values() for m in data["marks"]]
    print(f"The class average is{sum(val)/len(val):.2f}")
   
def avg():
    print("\n displaing average scores for all studetns\n")
    for key,values in student.items():
        avg=[f"the averaage is{values["marks"]/len(values["marks"])}"]
        print(f"The average of roll no. {key} is {avg:.2f}")


def topper():
    top = max(student.items(), key=lambda x: sum(x[1]["marks"]) / len(x[1]["marks"]))
    name, course = top[1]["geninfo"]
    avg_score = sum(top[1]["marks"]) / len(top[1]["marks"])
    print(f"Topper is {name} ({course}) with average {avg_score:.2f}")
def stats():
    all_marks = [m for data in student.values() for m in data["marks"]]
    print("Class Average:", sum(all_marks)/len(all_marks))
    print("Highest Mark:", max(all_marks))
    print("Lowest Mark:", min(all_marks))

ask()
