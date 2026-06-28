employees = {}

def add_employee():
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    salary = float(input("Enter Salary: "))
    employees[emp_id] = {"name": name, "dept": dept, "salary": salary}
    print("Employee added\n")

def display_employees():
    if not employees:
        print("No records\n")
    else:
        for emp_id, data in employees.items():
            print(f"ID:{emp_id}, Name:{data['name']}, Dept:{data['dept']}, Salary:{data['salary']}")
        print()

def search_employee():
    emp_id = int(input("Enter ID to search: "))
    if emp_id in employees:
        d = employees[emp_id]
        print(f"Found → ID:{emp_id}, Name:{d['name']}, Dept:{d['dept']}, Salary:{d['salary']}\n")
    else:
        print("Not found\n")

def update_employee():
    emp_id = int(input("Enter ID to update: "))
    if emp_id in employees:
        name = input("Enter new Name: ")
        dept = input("Enter new Dept: ")
        salary = float(input("Enter new Salary: "))
        employees[emp_id] = {"name": name, "dept": dept, "salary": salary}
        print("Updated\n")
    else:
        print("Not found\n")

def delete_employee():
    emp_id = int(input("Enter ID to delete: "))
    if emp_id in employees:
        del employees[emp_id]
        print("Deleted\n")
    else:
        print("Not found\n")

def average_salary():
    if employees:
        avg = sum(d["salary"] for d in employees.values())/len(employees)
        print(f"Average Salary: {avg:.2f}\n")
    else:
        print("No records\n")

def report():
    print("Final Report")
    display_employees()
    average_salary()
    print("Conclusion: System executed successfully\n")

def menu():
    while True:
        print("1.Add 2.Display 3.Search 4.Update 5.Delete 6.Average Salary 7.Report 8.Exit")
        ch = input("Choice: ")
        if ch=="1": add_employee()
        elif ch=="2": display_employees()
        elif ch=="3": search_employee()
        elif ch=="4": update_employee()
        elif ch=="5": delete_employee()
        elif ch=="6": average_salary()
        elif ch=="7": report()
        elif ch=="8": break
        else: print("Invalid\n")

menu()
