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
    },
    "hot chocolate": {
        "ingredients": {
            "water": 200,
            "milk": 100,
            "hot chocolate powder": 50,
        },
        "cost": 2.75,
    },
    "very berry ice cooler": {
        "ingredients": {
            "water": 150,
            "ice": 100,
            "frozen berries": 50,
            "fruit juice": 50,
        },
        "cost": 3.0,
        }
    }


resources = {
    "water": 1000,
    "ice": 500,
    "milk": 500,
    "coffee": 200,
    "hot chocolate powder": 200,
    "frozen berries": 200,
    "fruit juice": 200,
    "money": 0,
}

# TODO: 1. Print report of all coffee machine resources


def report():
    print("----------------------------------------------")
    print("Report")
    for resource in resources:
        print(f"{resource.capitalize()}: {resources[resource]}")
    print("----------------------------------------------")

# TODO: 2. Check resources sufficient to make drink order


def check_resources(input_selection):
    failure_report = []
    failure_message = "Sorry there is not enough:"
    for ingredient in MENU[input_selection]["ingredients"]:
        if MENU[input_selection]["ingredients"][ingredient] > resources[ingredient]:
            failure_report.append(ingredient)
    if len(failure_report) > 0:
        for ingredient in failure_report:
            if failure_report[-1] == ingredient:
                failure_message += f" {ingredient}."
            else:
                failure_message += f" {ingredient},"

        return failure_message
    else:
        return True

# TODO: 3. Process coins, add profit to resources, return change owed


def accept_coins(input_selection):
    input_coins = {"Quarter": int(input("How many quarters? ")), "Dime": int(input("How many dimes? ")),
                   "Nickel": int(input("How many nickels? ")), "Pennies": int(input("How many pennies? "))}
    multiplier = {"Quarter": 25, "Dime": 10, "Nickel": 5, "Pennies": 1}
    sum = 0
    change = 0
    for coin in input_coins:
        sum += round(float((input_coins[coin] * multiplier[coin]) / 100), 2)
    if sum >= MENU[input_selection]["cost"]:
        resources["money"] += MENU[input_selection]["cost"]
        change += round((sum - MENU[input_selection]["cost"]), 2)
        return change

    else:
        return True


# TODO: 4. Deduct drink selection from resources.
def take_from_resources(input_selection):
    for ingredient in MENU[input_selection]["ingredients"]:
        resources[ingredient] -= MENU[input_selection]["ingredients"][ingredient]


# TODO: 5. Print menu
def menu():
    print("----------------------------------------------")
    print("Menu:")
    for item in MENU:
        print(f"{item.capitalize()}, ${MENU[item]['cost']}")
    print("----------------------------------------------")

# TODO: 6. Make coffee machine


def refill():
    global resources
    max_resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    for resource in max_resources:
        top_up = (max_resources[resource] - resources[resource])
        if resource == "coffee" and top_up != 0:
            print(f"To refill, please add {top_up}g of {resource}")
        elif top_up != 0:
            print(f"To refill, please add {top_up}ml of {resource}")
    print("")
    refill_status = input("Have you refilled the machine? Type 'yes or 'no': ").lower()
    if refill_status == "yes":
        for resource in max_resources:
            resources[resource] = max_resources[resource]


def coffee_machine():
    on_status = True
    while on_status:
        selection_pass = False
        while not selection_pass:
            menu()
            selection = input("What drink would you like, type item from menu: ").lower()
            if selection == "off":
                print("Goodbye.")
                return
            elif selection == "report":
                report()
            elif selection == "refill":
                refill()
            elif selection in MENU and selection != "refill":
                selection_pass = True
            else:
                print("Not a valid input.")
        check_res = check_resources(selection)
        if check_res == False:
            print(check_res)

        else:
            payment = accept_coins(selection)

            if payment == True:
                print("Sorry that's not enough money. Money refunded.")
            if payment != 0:
                print(f"Here is ${payment} in change.")
            if payment >= 0:
                print(f"Here is your {selection}, enjoy!")
                print("")
                take_from_resources(selection)


# TODO: 7.

coffee_machine()

# Just a much, much, much longer comment!
