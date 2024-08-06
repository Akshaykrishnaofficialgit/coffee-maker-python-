MENU = {
    "espresso": {
        "ingredients": {
            "water": 15,
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
        "cost": 3.0
    }
}

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(resource,chosen_drink):
    for item in chosen_drink:
        if chosen_drink[item]>resource[item]:
            print(f"sorry there is no enough {item}")
            return False
    return True

def payment_portal():
    print("please insert the coins.")
    total = int(input("How many quarters"))*0.25
    total += int(input("How many Dimes")) * 0.10
    total += int(input("How many Nickel")) * 0.05
    total += int(input("How many quarters")) * 0.01
    return total
def payment_acceptance(amount,drink_cost):
    if amount>=drink_cost:
        balance=round(amount-drink_cost,2)
        print(f"Here is your balance amount ${balance}")
        global profit
        profit+=drink_cost
        return True
    else:
        print("There is no sufficient amount of money")
        return False

def make_coffee(resources,item_resources,drink_name):
    for item in item_resources:
        resources[item] -= item_resources[item]
    print(f"Here is your {drink_name},Enjoy!")

profit=0
is_on = True
while is_on:
    choice = input("What would you like?(espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water:{RESOURCES['water']}")
        print(f"Milk:{RESOURCES['milk']}")
        print(f"Coffee:{RESOURCES['coffee']}")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(RESOURCES,drink["ingredients"]):
            payment = payment_portal()
            if payment_acceptance(payment,drink["cost"]):
                make_coffee(RESOURCES,drink["ingredients"],choice)




