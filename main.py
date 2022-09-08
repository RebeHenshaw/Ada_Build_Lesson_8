inventory = [
    {
        'name': 'Ada Chips',
        'item_number': 'A1',
        'price': 0.50,
        'quantity': 5

    },
    {
        'name': 'Ada Candy Bar',
        'item_number': 'A2',
        'price': 0.75,
        'quantity': 5
    },
    {
        'name': 'Ada Gum',
        'item_number': 'A3',
        'price': 0.25,
        'quantity': 5
    },
]
choice = 'A2'
funds = 1.00


def buy(items, selected, money):
    """Conduct buying process."""
    print("Welcome to Ada's Vending Machine!\nHere are the available items:")
    display_inventory(items)
    price, updated_items = get_values(items, selected)
    confirm_funds(price, money)
    print("\nUpdated inventory below:\n")
    display_inventory(updated_items)


def get_values(items, selected):
    """Confirm choice is valid and update inventory"""
    for each in items:
        if each['item_number'] == selected:
            each['quantity'] = each['quantity'] - 1
            return each['price'], items
    print("Invalid choice")
    quit()


def display_inventory(products):
    """Show inventory of vending machine."""
    for each in products:
        print(f"""-\nName: {each['name']}\nVending Machine Number: {each['item_number']}\
\nPrice: ${each['price']:.2f}\nQuantity: {each['quantity']}""")


def confirm_funds(price, money):
    """Confirm funds are sufficient and give change or raise error."""
    if price <= money:
        change = money - price
        print(f"\nThank you, your change is ${change:.2f}.")
    else:
        print("Not enough money for selection.")
        quit()


buy(inventory, choice, funds)
