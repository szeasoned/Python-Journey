import json
import csv

student_infos = []

# HOW MANY STUDENTS TO RECORD
while True:
    try:
        student_counts = int(input("How many student/s to enter: "))
        if student_counts < 0:
            print("Enter a positive value!")
            continue
        else:
            break
    except ValueError:
        print("Enter a VALID value!")
        continue

# ASK THE STUDENT'S NAME, AGE UNTIL GIVEN STUDENT COUNT IS REACHED
student_count = 0

while student_count < student_counts:
    student_info = []
    total_score = 0
    quiz_count = 0
    name = input("Enter student name: ")
    student_info.append(name)
    while True:
        try:
            age = int(input(f"Enter {name}'s age: "))
            student_info.append(age)
            student_count += 1
            if age < 0:
                print(f"{name} is already learning!")
                continue
            else:
                break
        except ValueError:
            print("Invalid age!")
            continue

# ASK THE STUDENT'S QUIZ SCORE 1-3 FOR EVERY STUDENT
    quiz_count = 1
    while quiz_count < 4:
        try:
            quiz_score = int(input(f"Enter quiz {quiz_count} score  (0-100): "))
            if quiz_score < 0 or quiz_score > 100:
                print("Enter a score from 0-100!")
            else:
                quiz_count += 1
                total_score += quiz_score
        except ValueError:
            print(f"Invalid quiz {quiz_count} score!")

    if quiz_count == 3:
        average_grade = total_score / 3

# CALCULATE AVERAGE
    letter_grade = ""
    average_grade = total_score / 3
    student_info.append(average_grade)
    if average_grade < 60:
        letter_grade = "F"
    elif average_grade <= 69:
        letter_grade = "D"
    elif average_grade <= 79:
        letter_grade = "C"
    elif average_grade <= 89:
        letter_grade = "B"
    elif average_grade >= 90:
        letter_grade = "A"
    student_info.append(letter_grade)
    student_infos.append(student_info)


file_path = "student_report.txt"
final_data = ""

head_note = "========== STUDENT REPORT ==========\n"
main_body_data = ""
body_data = ""
body_separator = "------------------------------------"
foot_note = "===================================="

student_count = 0

for student in student_infos:
    student_data = (
        f"\nName: {student[0]}\n"
        f"Age: {student[1]}\n"
        f"Average: {student[2]}\n"
        f"Letter Grade: {student[3]}\n"
    )

    main_body_data += student_data
    student_count += 1

    if student_count < len(student_infos):
        main_body_data += "\n" + body_separator + "\n"

    final_data = head_note + main_body_data + "\n" + foot_note

with open(file_path, "w") as file:
    file.write(final_data)