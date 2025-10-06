# Taco Palace Ordering System

# Creating a table using a list (per zyBook 5.20)
# Menu items and prices stored in a table
menu_items = {
    1: ("Taco", 3.50),
    2: ("Burrito", 4.50),
    3: ("Nachos", 3.00),
    4: ("Soft Drink", 4.00)
}

# List to store ordered items
order_list = []

# Total price holder
total_price = 0.0


# Function to display the menu
def print_menu():
    print("--- Taco Palace Menu ---\n")
    for i in menu_items:
        # Print row and column pair: e.g. menu_items[0][0]= tacos; menu_items[0][1]= 3.50
        print(f"{i}. {menu_items[i][0]} - ${menu_items[i][1]:.2f}")
    print("5. Quit")


# Function to get price of an item
def get_item_price(item_number):
    return menu_items[item_number][1]


# Function to get name of an item
def get_item_name(item_number):
    return menu_items[item_number][0]


# Welcome message
print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection")

# Main loop
is_order_incomplete = True
while is_order_incomplete:
    print_menu()
    selection = int(input("Enter your selection (1-5): "))
    if selection == 5:
            print("Thank you for ordering at Taco Palace!\n")
            print("Here is your order summary:")
            for item in order_list:
                print(f"- {item}")
            print(f"Total amount due: ${total_price:.2f}")
            is_order_incomplete = False
    elif selection in menu_items:
        item_name = get_item_name(selection)
        item_price = get_item_price(selection)
        print(f"You have selected {item_name}.")
        order_list.append(item_name)
        total_price += item_price
    # waring the user that the input is invalid
    else:
        print("Invalid selection. Please choose a number from the menu.")