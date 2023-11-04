from data import menu, resources

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = resources["money"]
flag = True


def report():
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}")


def reqCheck(a):
    if a == "espresso":
        if water >= menu[a]["ingredients"]["water"]:
            if coffee >= menu[a]["ingredients"]["coffee"]:
                return True
            else:
                return False
        else:
            return False
    else:
        if water >= menu[a]["ingredients"]["water"]:
            if coffee >= menu[a]["ingredients"]["coffee"]:
                if milk >= menu[a]["ingredients"]["milk"]:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


def makeCoffee(type, resources):
    try:
        reqWater = menu[type]["ingredients"]["water"]
        resources["water"] -= reqWater
        reqCoffee = menu[type]["ingredients"]["coffee"]
        resources["coffee"] -= reqCoffee
        reqMilk = menu[type]["ingredients"]["milk"]
        resources["milk"] -= reqMilk
    except KeyError:
        pass


def bill(type, resources):
    coins = [0.01, 0.05, 0.10, 0.25]
    pennies = int(input("How many pennies?\n"))
    nickles = int(input("How many nickles?\n"))
    dimes = int(input("How many dimes?\n"))
    quarters = int(input("How many quarters?\n"))
    paid = (
        (pennies * coins[0])
        + (nickles * coins[1])
        + (dimes * coins[2])
        + (quarters * coins[3])
    )
    if paid > menu[type]["cost"]:
        change = paid - menu[type]["cost"]
        resources["money"] += menu[type]["cost"]
        print(f"Here is ${change} in change. Enjoy your {type}!.\n")
    elif paid == menu[type]["cost"]:
        print(f"Here is your {type}. Enjoy!\n")
    else:
        print("Sorry that's not enough money. Money refunded.\n")


while flag:
    print("What would you like to order today? (Espresso, Latte, Cappucino)")
    coffeeChoice = input().lower()
    match (coffeeChoice):
        case "report":
            report()
            break
        case "espresso":
            if reqCheck("espresso"):
                makeCoffee("espresso", resources)
                bill("espresso", resources)
            else:
                print("Insufficient Ingredients. Check report for more details")
            break
        case "latte":
            if reqCheck("latte"):
                makeCoffee("latte", resources)
                bill("latte", resources)
            else:
                print("Insufficient Ingredients. Check report for more details")
            break
        case "cappucino":
            if reqCheck("cappucino"):
                makeCoffee("cappucino", resources)
                bill("cappucino", resources)
            else:
                print("Insufficient Ingredients. Check report for more details")
            break
        case "off":
            print("Coffee machine is now turned off")
            flag = False
            break
        case _:
            print("Invalid choice. Try again.")
            break
