text_data = ""
file_path = "journal.txt"

username = input("Please enter your name: ")
date = input("Enter date (yyyy/mm/dd): ")
lesson = input("Enter one thing that you've learn today: ")

text_data = ("----- Daily Journal -----\n"
             f"Name: {username}\n"
             f"Date: {date}\n"
             f"Lesson: {lesson}\n"
             "-------------------------")
with open(file_path, "w") as file:
    file.write(text_data)