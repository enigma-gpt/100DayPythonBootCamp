MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

earned_money = 0
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]


coffee_type = input('What would you like? (espresso/latte/cappuccino)')

while coffee_type != "off":

    if coffee_type == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${earned_money}")

    elif coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino" :
        print('Please insert coins.')

        quarters = int(input('how many quarters?:'))
        dimes = int(input('how many dimes?:'))
        nickles = int(input('how many nickles?:'))
        pennies = int(input('how many pennies?:'))

        money_total = ((quarters * 25) + (dimes * 10) + (nickles * 5) + pennies) / 100
        print(f'total money = {money_total}')

        coffee_cost = MENU[coffee_type]['cost']
        print(f'coffee cost = {coffee_cost}')

        if money_total < coffee_cost:
            print("Sorry that's not enough money. Money refunded.")
        else:

            print(f"Here is ${round(money_total - coffee_cost, 2)} in change.")
            print(f"Here is your {coffee_type}. Enjoy!")

            water -= int(MENU[coffee_type]['ingredients']['water'])
            coffee -= int(MENU[coffee_type]['ingredients']['coffee'])

            maybe_milk = MENU[coffee_type]['ingredients']
            if 'milk' in maybe_milk:
                milk -= int(maybe_milk['milk'])

            earned_money += coffee_cost

    else:
        print('wrong input')

    coffee_type = input('What would you like? (espresso/latte/cappuccino)')