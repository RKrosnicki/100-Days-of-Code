MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18.5,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_price(price, cash):
    if cash < price:
        return False
    else:
        return True


def make_an_order():
    for coffee in MENU:
        print(f"{coffee}: ${MENU[coffee]['cost']}")
    order = input("What would you like? (espresso/latte/cappuccino) ").lower()
    return order


def insert_coins():
    print("Insert coins:")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def check_resources_v2(order_ingredients):
    result = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there's not enough {item}!")
            result = False
    return result


# def check_resources(order):
#     if resources["water"] < MENU[order]["ingredients"]["water"]:
#          print("Sorry, there's not enough water.")
#          return False
#     elif resources["milk"] < MENU[order]["ingredients"]["milk"]:
#           print("Sorry, there's not enough milk.")
#           return False
#     elif resources["coffee"] < MENU[order]["ingredients"]["coffee"]:
#         print("Sorry, there's not enough coffee.")
#         return False
#     else:
#         resources["water"] -=  MENU[order]["ingredients"]["water"]
#         resources["milk"] -= MENU[order]["ingredients"]["milk"]
#         resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
#         return True


go_on = True
resources["money"] = 0

while go_on:
    order = make_an_order()

    while order == "report":
        if resources["money"] == 0:
            print(f"\nWater: {resources['water']}ml"
                  f"\nMilk: {resources['milk']}ml"
                  f"\nCeffee: {resources['coffee']}g\n")
            order = make_an_order()
            if order == "off":
                go_on = False
                break
        else:
            print(
                f"\nWater: {resources['water']}ml"
                f"\nMilk: {resources['milk']}ml"
                f"\nCeffee: {resources['coffee']}g"
                f"\nMoney: ${resources['money']}\n")
            order = make_an_order()
            if order == "off":
                go_on = False
                break

    if order != "off":
        if check_resources_v2(MENU[order]['ingredients']):
            cash_provided = insert_coins()
            if check_price(MENU[order]["cost"], cash_provided):
                resources["money"] += MENU[order]["cost"]
                print(f"\nHere's your change: ${round(cash_provided - MENU[order]['cost'], 2)}")
                print(f"Here's your {order}, enjoy!\n")
                for item in MENU[order]['ingredients']:
                    resources[item] -= MENU[order]['ingredients'][item]
            else:
                print(
                    f"\nNot enough money, your drink costs ${MENU[order]['cost']}, and you provided only ${cash_provided}.\n")
    else:
        go_on = False
