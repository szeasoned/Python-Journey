counter = 0
items = []

while True:
    try:
        item_count = int(input("How many items will you buy?: "))
        if item_count <= 0:
            print("Enter an appropriate amount!")
            continue
        else:
            break
    except ValueError:
        print("Enter a valid number!")
        continue

while True:
    if counter < item_count:
        item = input("Enter the item you want to buy: ")
        items.append(item)
        counter += 1
    else:
        break

# WRITE THE FILE
number = 0
file_path = "shopping_list.txt"
text_data = ("Shopping List\n"
            "-------------\n")
for item in items:
    number += 1
    text_data += (f"{number}. {item}\n")

with open(file_path, "w") as file:
    file.write(text_data)
    print("File successfully created!")