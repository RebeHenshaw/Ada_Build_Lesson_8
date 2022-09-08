class VendingMachine:
    def __init__(self):
        self.inventory = []
        self.welcome = "Welcome to Vending Machine!\nHere's your options:"

    def __str__(self):
        for each in self.inventory:
            print(each)

    def add_item(self, item):
        for each in self.inventory:
            if each['name'] == item.item_name:
                each['quantity'] += item.quantity
                return
        self.inventory.append({'name': item.item_name, 'item_number': item.number,
                               'price': item.price, 'quantity': item.quantity})
        return

    def display(self):
        for each in self.inventory:
            print(f"""-\nName: {each['name']}\nVending Machine Number: {each['item_number']}\
        \nPrice: ${each['price']:.2f}\nQuantity: {each['quantity']}""")

    def purchase_item(self, item, money):
        print(self.welcome)
        self.display()
        for each in self.inventory:
            if each['name'] == item.item_name:
                if money >= item.price:
                    each['quantity'] -= 1
                    print(f"\nThanks. Your change is ${money - item.price :.2f}\nYour updated items below:\n")
                    self.display()
                    quit()
                else:
                    print("Not enough money for selection. Please try again.")
                    quit()
        print("Invalid item selection, please try again")
        quit()


class Item:
    def __init__(self, machine_name, price, quantity, number, item_name):
        self.item_name = item_name
        self.number = number
        self.quantity = quantity
        self.price = price
        self.machine_name = machine_name


snack_machine = VendingMachine()
drinks = VendingMachine()

chips = Item(snack_machine, .5, 5, 'A1', 'Ada Chips')
snack_machine.add_item(chips)
chips2 = Item(snack_machine, .5, 1, 'A1', 'Ada Chips')
snack_machine.add_item(chips2)
candy = Item(snack_machine, .75, 4, 'A2', 'Candy Bar')
candy1 = Item(snack_machine, .75, 2, 'A2', 'Candy Bar')
snack_machine.add_item(candy)
snack_machine.add_item(candy1)
gum = Item(snack_machine, .25, 6, 'A3', 'Ada gum')
snack_machine.add_item(gum)
coffee = Item(drinks, 1.25, 6, 'A1', 'coffee')
drinks.add_item(coffee)
#snack_machine.purchase_item(gum, 1)
drinks.purchase_item(coffee, 5)


