from coffee_config import MENU, RESOURCE


def check_resource(coffee_ingredients):
    is_there_enough = True
    ingredients_available = RESOURCE['ingredients']

    for item in ingredients_available:
        if coffee_ingredients[item] > ingredients_available[item]:
            print(rf"Sorry there is not enough {item}")
            return False

    return is_there_enough

def show_report():
    ingredients = RESOURCE['ingredients']
    for item in ingredients:
        unit = 'ml' # the most common one is ml
        # give units for items
        if item == 'coffee':
            unit = 'g'
        print(rf"{item}: {ingredients[item]}{unit}") 

    print(rf"money: {RESOURCE['money']}$") 

def get_user_payment():
    quarters = int(input("Enter the number of quarters: "))      
    dimes = int(input("Enter the number of dimes: "))            
    nickels = int(input("Enter the number of nickels: "))        
    pennies = int(input("Enter the number of pennies: "))       

    total_cents = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies *0.01
    return total_cents

def check_payment(coffee_price, total_cents):
    # if it is not enough always return as False
    if coffee_price > total_cents:
        print("Sorry that's not enough money. Money refunded.")
        return False
    return True

def calculate_resource(coffee_ingredients, coffee_price, total_cents):
    ingredients_available = RESOURCE['ingredients']
    
    if total_cents > coffee_price:
        print(rf"Here is ${round(total_cents -float(coffee_price), 2)} dollars in change")

    # deducing the resources
    for item in ingredients_available:
        ingredients_available[item] = ingredients_available[item] - coffee_ingredients[item]
    
    # calculating revenue
    RESOURCE['money']+= float(coffee_price)




def start_coffee_machine():
    is_machine_on = True
    while is_machine_on:
        selected_coffee = input(rf'What would you like? (espresso/latte/cappuccino):')
        # Check if the user input is valid
        if selected_coffee in MENU.keys():
            ingredients = MENU[selected_coffee]['ingredients']
            coffee_price = MENU[selected_coffee]['cost']
            #Check if there are enough resource to make the selected coffee
            if check_resource(coffee_ingredients = ingredients):
                total_cents = get_user_payment()
                if check_payment(coffee_price =  coffee_price, total_cents= total_cents):
                    calculate_resource(ingredients, coffee_price, total_cents)
                    print(f"Here is your {selected_coffee}. Enjoy!")



        elif selected_coffee == 'report':
            show_report()
        # Turn off the coffee machine
        elif selected_coffee == 'off':
            is_machine_on = False
        else:
            print("The choice you selected does not exist, check it if you typed write the coffee.")

if __name__ == "__main__":
    start_coffee_machine()
