employee = {}

# employee = {101 : {"Name" : "Dhvit", "Age" : 21 , "Department" : "Data Science" , "Salary" : 500000}}


def add_employee(emp_id, name, age, department, salary):
    employee[emp_id] = {"Name" : name, "Age" : age, "Department" : department, "Salary" : salary}

    print("Employee added successfully!")

def view_all_employee():
    if employee == {}:
        print("No employee found...!!!")
    else:
        print("Employee ID | Name | Age | Department | Salary")
        for emp_id, details in employee.items():
            print(f"{emp_id} | {details['Name']} | {details['Age']} | {details['Department']} | {details['Salary']}")

def search_employee(emp_id):
    if emp_id in employee:
        details = employee[emp_id]
        print(f"Employee ID: {emp_id}")
        print(f"Name: {details['Name']}")
        print(f"Age: {details['Age']}")
        print(f"Department: {details['Department']}")
        print(f"Salary: {details['Salary']}")
    else:
        print("Employee not found.")


def main():

    while True:
        print("1. Add Employee")
        print("2. View All Employee")
        print("3. Search for Employee")
        print("4. Exit")

        choice = int(input("Select an option (1-4): "))

        if (choice == 1):

            emp_id = int(input("Enter Employee ID: "))
            if emp_id in employee:
                print("Employee ID already exists. Please try again.")
                return
            name = input("Enter Employee Name: ")
            age = int(input("Employee Age: "))
            department = input("Enter Employee Department: ")
            salary = int(input("Enter Employee Salary: "))
            add_employee(emp_id, name, age, department, salary)

        elif (choice == 2):
            view_all_employee()
        
        elif (choice == 3):
            emp_id = int(input("Enter Employee ID to Search: "))
            search_employee(emp_id)

        elif (choice == 4):
            print("Exiting the program...  GooooodBye!!")
            break

if __name__ == "__main__":
    main()

