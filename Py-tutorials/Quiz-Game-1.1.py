# Create a 5 question quiz game
# Will ask the user to try again if and only if they got 60% or lower
# Enter a key to retry and press any other key to quit

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

while True:
    score = 0
    question_num = 0
    guesses = []
    
    for question in questions:
        print("----------------")
        print(question)
        for choice in choices[question_num]:
            print(choice)
        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        
        if guess == answers[question_num]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
        
        question_num += 1
    score = round(score / len(questions) * 100)
    
    if score > 60:
        break
    else:
        print("------------------------------------------------")
        print(f"You got {score:g}%! Thanks for participating!")
        retry = input("Press '1' to try again. Press any other key to quit. ")
        if retry == "1":
            continue
        else:
            break

print("------------------------------------------------")
print("---------------------RESULT---------------------")
print("The correct answers are: ", end='')
for answer in answers:
    print(answer, end=' ')
print()

print("Your guess are: ", end='')
for guess in guesses:
    print(guess, end=' ')
print()
print(f"You got {score:g}%! Thanks for participating!")
print("------------------------------------------------")

