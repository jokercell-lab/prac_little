MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# print(MENU["espresso"]["ingredients"])

# TODO: which cafe do you want?
money = 0
cafe_start = True


def resource(order):
    """Return True  when resource enough"""
    for item in order:
        if order[item] >= resources[item]:
            print(f"Run ou tof {item}")
            return False
    return True


 # TODO: transaction success or not & money of add coin, and money upgrade
def coin_process():
    """Return total money"""
    print('please insert your coin')
    total = int(input("How many 1 coin:"))*1
    total += int(input("How many 5 coin:"))*5
    total += int(input("How many 10 coin:"))*10
    total += int(input("How many 50 coin:"))*50
    return total
    #return f"Enjoy your {user_cafe}"  # TODO: make a cafe


def transaction(receive_money, drink_cost):
    if drink_cost > receive_money:
        print("NOT enough money")
        return False
    else:
        change = receive_money - drink_cost
        print(f"Here is your change ${change}")
        global money
        money += drink_cost
        return True


def cafe_make(cafe_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {cafe_name}")

# def tran_money(x1, x2, x3, x4, mm):
#     mm = mm + x1 * 1 + x2 * 5 + x3 * 10 + x4 * 50
#     total = money + mm
#     cafe_price = MENU[user_cafe]["cost"]
#     if mm < cafe_price:
#         return "MONEY is NOT ENOUGH"
#     else:
#         return f"Here is ${mm} in charge"

# def cafe_make(user_cafe):
#     n1 = resources["water"] - MENU[user_cafe]["ingredients"]["water"]
#     n2 = resources["milk"] - MENU[user_cafe]["ingredients"]["milk"]
#     n3 = resources["coffee"] - MENU[user_cafe]["ingredients"]["coffee"]
#     resources["water"] = n1
#     resources["milk"] = n2
#     resources["coffee"] = n3
#     if n1 < 0 or n2 < 0 or n3 < 0:
#         return "Run out of resources"
#     else:
#         # print(tran_money(coin1, coin5, coin10, coin50, money))
#         return f"Enjoy your {user_cafe}"
# def situation():
#     if user_cafe == "report":
#         return f'Water: {resources["water"]} ml\nMilk: {resources["milk"]} ml\nCoffee:{resources["coffee"]} g\nMoney:{money}'
#     # TODO: making cafe situation, whether resource enough or not
#     else:  # TODO: resource decent after cafe was made
#         n1 = resources["water"] - MENU[user_cafe]["ingredients"]["water"]
#         n2 = resources["milk"] - MENU[user_cafe]["ingredients"]["milk"]
#         n3 = resources["coffee"] - MENU[user_cafe]["ingredients"]["coffee"]
#         resources["water"] = n1  # TODO: report current resources
#         resources["milk"] = n2
#         resources["coffee"] = n3
#         if n1 < 0 or n2 < 0 or n3 < 0:
#             return "Run out of resources"


while cafe_start:
    want_cafe = input("Do you want a cafe? y/n: ").lower()
    if want_cafe == "n":
        cafe_start = False
    else:
        user_cafe = input("Which one do you like?\n (espresso/latte/cappuccino): ").lower()
        if user_cafe == "report":
            print(f'Water: {resources["water"]} ml\nMilk: {resources["milk"]} ml\nCoffee:{resources["coffee"]} g\nMoney:{money}')

        # TODO: making cafe situation, whether resource enough or not
        else:
            drink = MENU[user_cafe]
            if resource(drink["ingredients"]):
                pay = coin_process()
                if transaction(pay, drink["cost"]):
                    cafe_make(user_cafe, drink["ingredients"])









# n1 = resources["water"] - MENU[user_cafe]["ingredients"]["water"]
# n2 = resources["milk"] - MENU[user_cafe]["ingredients"]["milk"]
# n3 = resources["coffee"] - MENU[user_cafe]["ingredients"]["coffee"]
# resources["water"] = n1  # TODO: report current resources
# resources["milk"] = n2
# resources["coffee"] = n3
# if n1 < 0 or n2 < 0 or n3 < 0:
#     print("Run out of resources")

