# Coffee Machine Resources
resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}

# Drink details
drinks = {
    'e': {'name': 'Espresso', 'water': 50, 'milk': 0, 'coffee': 18, 'cost': 1.50},
    'l': {'name': 'Latte', 'water': 200, 'milk': 150, 'coffee': 24, 'cost': 2.50},
    'c': {'name': 'Cappuccino', 'water': 250, 'milk': 100, 'coffee': 24, 'cost': 3.00}
}

def display_report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']:.2f}")

def check_resources(water, milk, coffee):
    return resources['water'] >= water and resources['milk'] >= milk and resources['coffee'] >= coffee

def process_coins():
    print("Please insert coins.")
    quarters = int(input("Quarters: ")) * 0.25
    dimes = int(input("Dimes: ")) * 0.10
    nickels = int(input("Nickels: ")) * 0.05
    pennies = int(input("Pennies: ")) * 0.01
    total_coins = quarters + dimes + nickels + pennies
    return total_coins

def make_coffee(drink, cost):
    resources['water'] -= drink['water']
    resources['milk'] -= drink['milk']
    resources['coffee'] -= drink['coffee']
    resources['money'] += cost
    print(f"Here is your {drink['name']}. Enjoy!")

def get_drink_details(drink_type):
    return drinks.get(drink_type)

def coffee_machine():
    while True:
        print("\nAvailable Drinks:")
        for key, drink in drinks.items():
            print(f"{key} - {drink['name']} (${drink['cost']:.2f}): {drink['water']}ml water, {drink['milk']}ml milk, {drink['coffee']}g coffee")

        user_input = input("\nWhat would you like? (e/ l/ c/ q): ").lower()

        if user_input == 'q':
            break
        elif user_input == 'report':
            display_report()
        elif user_input in drinks:
            drink = get_drink_details(user_input)
            print(f"Cost: ${drink['cost']:.2f}")
            print(f"Resources left - Water: {resources['water']}ml, Milk: {resources['milk']}ml, Coffee: {resources['coffee']}g")
            if check_resources(drink['water'], drink['milk'], drink['coffee']):
                cost = process_coins()
                if cost >= drink['cost']:
                    make_coffee(drink, drink['cost'])
                    change = cost - drink['cost']
                    if change > 0:
                        print(f"Here is ${change:.2f} dollars in change.")
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print(f"Sorry, not enough resources to make {drink['name']}.")
        else:
            print("Invalid input. Please try again.")

# Run the Coffee Machine
coffee_machine()
