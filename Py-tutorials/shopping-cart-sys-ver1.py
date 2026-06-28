# create a shopping cart system

available_items = {"FUDGEEBAR": 10,
                   "HANSEL": 10,
                   "WATER": 15,
                   "PRETZEL": 20,
                   "MOBY": 12,
                   "COLA": 15,
                   "BEARBRAND": 18,
                   "TWINPACK": 20,
                   "MILO": 16,
                   "CRACKLINS": 12,
                   "PIER": 13}

print("------------ ITEMS ------------")
for key, value in available_items.items():
    print(f"{value} pesos - {key}")
print("-------------------------------")

cart = []
total = 0
cart_subtotal = []

while True:
    order = input("Enter your order/s: (Q to quit): ").upper()
    if order == 'Q':
        break
    elif order in available_items is not None:
        cart.append(order)

for order in cart:
    cart_subtotal.append(available_items.get(order))
    
for order in cart:
    total += available_items.get(order)

print()
print("----------- RECEIPT -----------")
print()
print(f"You ordered: ", end='')
    
for item in cart:
    print(item, end=' ')

print()
print(f"Your total bill is: {total}")

print()
print("-------------------------------")
print()

# new_cart = cart

while True:
    check_subtotal = input("Press '1' to view subtotal: ")
    print()
    
    print("----------- SUBTOTAL -----------")
    if check_subtotal != '1':
        break
    else:
        print("You ordered: ", end='')
        for item in cart:
            print(item, end=' ')
        
        print()
        print("The prices are: ", end='')
        for price in cart_subtotal:
            print(price, end=' ')
        print("--------------------------------")
        break