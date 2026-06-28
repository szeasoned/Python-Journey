import csv

file_path = "example.csv"
text = [["Name", "Age", "Grade"],
        ["Aaron", 17, "A"],
        ["Prince", 18, "B"]]

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    for row in text:
        writer.writerow(row)
