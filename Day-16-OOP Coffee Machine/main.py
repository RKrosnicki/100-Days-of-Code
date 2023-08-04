from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    #clear()  #comment it if you're on PyCharm
    print("Welcome in OOP coffee machine! \nHere's what you can order:")

    for item in menu.get_items().split("/"):
        price = menu.find_drink(item)
        if price:
            print(f"{item} - ${price.cost}")

    order = input("\nWhat are you drinking today? ").lower()
    ordered = menu.find_drink(order)

    if ordered:
        print(f"You've chosen {order}, it costs ${ordered.cost}\n")
        if coffee_maker.is_resource_sufficient(ordered):
            if money_machine.make_payment(ordered.cost):
                print(coffee_maker.make_coffee(ordered))
    else:
        if order == "report":
            print(coffee_maker.report())
            print(money_machine.report())
        elif order == "off":
            print("Turning off.\nGoodbye!")
            break
