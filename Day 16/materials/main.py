from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

selection = input(f"What would you like? {menu.get_items()}")

while selection != 'off':

    if selection == 'report':
        coffe_maker.report()
        money_machine.report()

    elif selection == 'latte' or selection == 'espresso' or selection == 'cappuccino':
        drink = menu.find_drink(selection)
        can_make = coffe_maker.is_resource_sufficient(drink)
        if can_make:
            if money_machine.make_payment(drink.cost):
                coffe_maker.make_coffee(drink)

    selection = input(f"What would you like? {menu.get_items()}")






