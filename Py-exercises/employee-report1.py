employee_infos =[]

while True:
    try:
        input_count = int(input("Enter employee count: "))
        if input_count <= 0:
            print("Enter a valid number of employee!")
            continue

        else:
            break

    except ValueError:
        print("Enter a numerical value!")
        continue

employee_count = 0

while input_count > employee_count:
    employee_info = []
    print("=====================================")

    name = input("Enter employee name: ")
    employee_info.append(name)

    department = input(f"Enter {name}'s department: ").upper()
    employee_info.append(department)

    employee_count += 1

    while True:
        try:
            yo_experience = int(input(f"Enter {name}'s years of experience: "))
            if yo_experience < 0:
                print("Enter a valid year!")
                continue
            else:
                employee_info.append(yo_experience)
                break
        except ValueError:
            print("Enter a numerical value!")
            continue

    level = ""

    if yo_experience <= 1:
        level = "Junior"
    elif yo_experience <= 5:
        level = "Mid-Level"
    elif yo_experience >= 6:
        level = "Senior"

    employee_info.append(level)

    while True:
        try:
            monthly_salary = float(input(f"Enter {name}'s monthly salary: "))
            if monthly_salary <= 0:
                print("Unemployed?")
                continue
            else:
                employee_info.append(monthly_salary)
                break
        except ValueError:
            print("Enter a numerical value!")
            continue
    employee_infos.append(employee_info)

# FORMATTING

header = "========== EMPLOYEE REPORT =========="
main_body = ""
body_separator = "------------------------------------"
footer = "====================================="

# BODY CONTENT AND ITERATION FOR TEXT FILE
employee_count = 0
for employee_info in employee_infos:
    body = (
        f"\nName: {employee_info[0]}\n"
        f"Department: {employee_info[1]}\n"
        f"Experience: {employee_info[2]} years\n"
        f"Salary: {employee_info[4]:.2f}\n"
        f"Level: {employee_info[3]}\n"
    )
    employee_count += 1
    main_body += body

    if employee_count < len(employee_infos):
        main_body += "\n" + body_separator + "\n"

full_details = header + "\n" + main_body + "\n" + footer

# BODY CONTENT AND ITERATION FOR JSON FILE


# WRITING TEXT

file_path_txt = "employee_report.txt"

# TEXT FILE
with open(file_path_txt, "w") as file:
    file.write(full_details)
