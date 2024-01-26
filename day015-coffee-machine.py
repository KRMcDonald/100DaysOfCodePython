MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


# TODO: prompt user
# TODO: be able to turn off the coffee machine
# TODO: print current report
# TODO: check resources are sufficient
# TODO: process coins
# TODO: check transaction successful
# TODO: make coffee

money_earned = float(0.0)


def prompt():
    selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if selection == "report":
        print_report()
        prompt()
    elif selection == "off":
        turn_off()
    else:
        check_sufficient_resources(selection)


def turn_off():
    print("Shutting down...")


def print_report():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources["water"]}g")
    print(f"Money: ${money_earned:.2f}")


def check_sufficient_resources(drink):
    drink_dict = MENU[drink]["ingredients"]
    if resources["water"] < drink_dict["water"] or resources["milk"] < drink_dict["milk"] or resources["coffee"] < drink_dict["coffee"]:
        print(f"Insufficient ingredients to make {drink}. Please choose a different option.")
        prompt()
    else:
        process_coins(drink)


def process_coins(drink):
    print(f'Please insert ${MENU[drink]["cost"]:.2f}')
    q = float(input("How many quarters? "))
    d = float(input("How many dimes? "))
    n = float(input("How many nickels? "))
    p = float(input("How many pennies? "))
    total_inserted = 0.25 * q + 0.1 * d + 0.05 * n + 0.01 * p
    if total_inserted < MENU[drink]["cost"]:
        print("Not enough coins inserted. You will be refunded and your order canceled.")
        prompt()
    else:
        print(f"Thank you. Your {drink} will be made.")
        global money_earned
        money_earned += MENU[drink]["cost"]
        if total_inserted > MENU[drink]["cost"]:
            change = total_inserted - MENU[drink]["cost"]
            print(f"Here is your change: ${change:.2f}")
        make_coffee(drink)


def make_coffee(drink):
    global resources
    drink_dict = MENU[drink]["ingredients"]
    resources["water"] -= drink_dict["water"]
    resources["milk"] -= drink_dict["milk"]
    resources["coffee"] -= drink_dict["coffee"]
    print(f"Here is your {drink}.")
    prompt()


prompt()
