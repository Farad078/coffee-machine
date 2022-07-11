from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

espresso = MenuItem('espresso', 50, 0, 18, 1.5)
latte = MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5)
cappuccino = MenuItem(name='cappuccino', water=250, milk=150, coffee=24, cost=3.0)

coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

is_on = True

while is_on:
    options = input(f"What would you like? {menu.get_items()}:")
    if options == 'off':
        is_on = False
    elif options == 'report':
        coffeemaker.report()
        moneymachine.report()
    elif options == latte.name:
        if (moneymachine.make_payment(latte.cost) == True) and (coffeemaker.is_resource_sufficient(latte) == True):
            coffeemaker.make_coffee(latte)
        else:
            coffeemaker.is_resource_sufficient(latte)
    elif options == espresso.name:
        if (moneymachine.make_payment(espresso.cost) == True) and (coffeemaker.is_resource_sufficient(espresso) == True):
            coffeemaker.make_coffee(espresso)
        else:
            coffeemaker.is_resource_sufficient(espresso)
    elif options == cappuccino.name:
        if (moneymachine.make_payment(cappuccino.cost) == True) and (coffeemaker.is_resource_sufficient(cappuccino) == True):
            coffeemaker.make_coffee(cappuccino)
        else:
            coffeemaker.is_resource_sufficient(cappuccino)






