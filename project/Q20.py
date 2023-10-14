# Restaurant menu
menu = {
    "Burger": 150,
    "Pizza": 500,
    "Pasta": 300,
    "Salad": 100,
    "Juice": 199,
}
order = {}

# display the menu
def display_menu():
    print("Menu:")
    for i, j in menu.items():
        print(f"{i}: {j}/")

# Function to place an order
def place_order():
    while True:
        item = input("Enter an item to order (or 'done' to finish): ")
        if item == 'done':
            break
        if item in menu:
            quantity = int(input(f"How many {item}s would you like to order? "))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
        else:
            print("Item not on the menu. Please choose from the menu items.")

def calculate_total(order):
    total = sum(menu[item] * quantity for item, quantity in order.items())
    return total

# Main program
print("Welcome to the Restaurant!")
display_menu()
place_order()

if order:
    print("\nYour order:")
    for item, quantity in order.items():
        print(f"{item}: {quantity}")
    total_cost = calculate_total(order)
    print(f"Total cost: {total_cost}/")
else:
    print("No items were ordered. Have a nice day!")

print("Thank you for dining with us!")
