# User Input and Verification
name = input("Enter your name: ")
section = input("Enter is your section/course: ")

quiz_scores = []
total_scores = 0
counter = 1

while True:
    if counter <= 3:
        try:
            quiz_score = int(input(f"Enter quiz {counter} score (0-100): "))
            if quiz_score < 0 or quiz_score > 100:
                print("Score is 0-100!")
                continue
            else:
                total_scores += quiz_score
                quiz_scores.append(quiz_score)
                counter += 1
        except ValueError:
            print("Enter a valid score!")
            continue
    else:
        break

# Grade Conversion
average_grade = total_scores / 3
grade_conversion = ""
if average_grade < 60:
    grade_conversion = "F"
elif average_grade <= 69:
    grade_conversion = "D"
elif average_grade <= 79:
    grade_conversion = "C"
elif average_grade <= 89:
    grade_conversion = "B"
elif average_grade >= 90:
    grade_conversion = "A"

# File Creation
file_path = "student_report.txt"
text_data = (
    "========== STUDENT REPORT ==========\n"
    f"Name: {name}\n"
    f"Course/Section: {section}\n"
    
    f"\nQuiz Scores:\n"
    f"Quiz 1: {quiz_scores[0]}\n"
    f"Quiz 2: {quiz_scores[1]}\n"
    f"Quiz 3: {quiz_scores[2]}\n"

    f"\nAverage: {average_grade:.2f}\n"
    f"Letter Grade: {grade_conversion}"
)

with open(file_path, "w") as file:
    file.write(text_data)
    print("File successfully created!")