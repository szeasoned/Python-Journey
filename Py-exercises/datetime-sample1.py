import datetime
import pygame

short_note = input("Enter a short note: ")

while True:
    double_check = input("Please recheck your note (c to confirm/quit): ").upper()
    if double_check == "C":
        break
    else:
        continue

date_today = datetime.datetime.now()
today = date_today.strftime("%Y-%m-%d")
current_time = date_today.strftime("%H:%M:%S")

note = (
    "==========================\n"
    f"\nDate: {today}\n"
    f"Time: {current_time}\n"
    f"Note: {short_note}"
)
file_path = "C:\\Users\\unhol\\OneDrive\\Desktop\\PYTHON-JOUREY\\notes.txt"

with open(file_path, "a") as file:
        file.write(note)

