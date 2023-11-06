from menu import Menu, MenuItem
from coffeemaker import CoffeeMaker
from moneymachine import MoneyMachine


menu = Menu()
coffeeMachine = CoffeeMaker()
moneyCounter = MoneyMachine()
isOn = True

while isOn:
    print("What would you like to order today?")
    print(menu.get_items())
    choice = input()
    if choice == "off":
        isOn = False
    elif choice == "report":
        coffeeMachine.report()
        moneyCounter.report()
    else:
        drink = menu.find_drink(choice)
        if coffeeMachine.is_resource_sufficient(drink):
            if moneyCounter.make_payment(drink.cost):
                coffeeMachine.make_coffee(drink)
