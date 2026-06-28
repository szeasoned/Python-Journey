"""

Write a Python program that:
Asks the user to enter their name.
Asks for three quiz scores (0–100).
Calculates the average score.
Displays the student's name, the average (rounded to 2 decimal places), and the corresponding grade:
90–100: A
80–89: B
70–79: C
60–69: D
Below 60: F

Sample Output:
Enter your name: Alex
Enter Quiz 1 score: 85
Enter Quiz 2 score: 92
Enter Quiz 3 score: 88

Student: Alex
Average: 88.33
Grade: B

"""

counter = 1
quiz_scores = 0

name = input("What is your name? ")
while True:
    quiz_score = input(f"Enter Quiz {counter} score: ")

    try:
        quiz_score = int(quiz_score)
    except ValueError:
        print("Enter a valid score!")
        continue

    if quiz_score < 0 or quiz_score > 100:
        print("Quiz score is 0-100 points ONLY!")
        continue
    else:
        quiz_scores += quiz_score
        average = quiz_scores / 3
        counter += 1

    if counter > 3:
        break

grade = ""
if average < 60:
    grade = "F"
elif average <= 69:
    grade = "D"
elif average <= 79:
    grade = "C"
elif average <= 89:
    grade = "B"
elif average >= 90:
    grade = "A"

print("-" * 25)
print(f"Student: {name}")
print(f"Average: {average:2f}")
print(f"Final Grade: {grade}")
print("-" * 25)