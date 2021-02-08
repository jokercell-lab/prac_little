from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cafe = CoffeeMaker() #print(cafe.resources)
menu = Menu()
money = MoneyMachine()


cafe_start = True
while cafe_start:
    options = menu.get_items()
    user_cafe = input(f"Please choose your cafe. {options}: ").lower()
    if user_cafe == "off":
        cafe_start = False
    elif user_cafe == "report":
        cafe.report()
        money.report()
    else:
        drink = menu.find_drink(user_cafe)
        if cafe.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                cafe.make_coffee(drink)


