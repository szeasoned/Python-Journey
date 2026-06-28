class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Food: {self.name}")
        print(f"Price: ₱{self.price}")

class Burger(Food):
    def __init__(self, name, price, patty_type):
        super().__init__(name, price)
        self.patty_type = patty_type

    def serve(self):
        print(f"{self.name} with {self.patty_type} patty is ready to serve.")

class Pizza(Food):
    def __init__(self, name, price, number_of_slice):
        super().__init__(name, price)
        self.number_of_slice = number_of_slice

    def serve(self):
        print(f"{self.name} with {self.number_of_slice} slices is ready to serve.")

class Drink(Food):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def serve(self):
        print(f"{self.size} {self.name} is ready to serve.")

burger1 = Burger("Cheeseburger", 120, "Beef")
pizza1 = Pizza("Pepperoni Pizza", 450, 8)
drink1 = Drink("Iced Tea", 50, "Large")

burger1.display_info()
burger1.serve()

pizza1.display_info()
pizza1.serve()

drink1.display_info()
drink1.serve()