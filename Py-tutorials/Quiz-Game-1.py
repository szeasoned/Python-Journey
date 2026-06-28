# Create a 5 question quiz game

questions = (("What is the capital of Australia?"),
             ("How many sides does a heptagon have?"),
             ("Who painted the Mona Lisa?"),
             ("What is the largest ocean on Earth?"),
             ("Which gas do plants absorb from the atmosphere during photosynthesis?"))

choices = (("A) Sydney","B) Melbourne","C) Canberra","D) Brisbane"),
           ("A) 5", "B) 6", "C) 7", "D) 8"),
           ("A) Michelangelo","B) Leonardo da Vinci","C) Raphael","D) Vincent van Gogh"),
           ("A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"),
           ("A) Oxygen", "B) Nitrogen", "C) Carbon dioxide", "D) Hydrogen"))

answers = ("C",
           "C",
           "B",
           "D",
           "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------")
    print(question)
    for choice in choices[question_num]:
        print(choice)
    
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("CORRECT!")
        score += 1
    else:
        print("INCORRECT!")
        print(f"The correct answer is: {answers[question_num]}")
    question_num += 1

score = int(score / len(questions) * 100)

print("--------RESULT--------")
print("The correct answers are: ", end='')

for answer in answers:
    print(answer, end=' ')
print()

print("Your answers are: ", end='')
for guess in guesses:
    print(guess, end=' ')
print()

print(f"Congratulations! You got {score}%")
if score >= 70:
    print("You passed! Thank you for joining!")
else:
    print("You failed! Try again!")
print("----------------------")
