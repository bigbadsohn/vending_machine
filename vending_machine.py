# Importing JSON File with vending machine items and price
import json

with open('items.json', 'r') as itemData:
    data = itemData.read()

obj = json.loads(data)

print(str(obj["gatorade"]))


# test example hashmap of items
items = {"cookie": 1.00, "coke": 0.75, "candy": 0.50}


# function checking if user input is valid

# INTRO
# welcome prompt
print("Welcome to Dennis's Vending Machine")

# list option of items user can purchase and price (from json file)


# BUYING PROCESS
# ask user to choose which item they want

# PAYMENT PROCESS
# ask user to enter money
# check if user inserted enough money for item

# POST PROCESSING
# if yes, give item and ask if they want to buy something else with extra money
# if yes repeat process
# if no give user change

# if no, ask user to enter more money
# if yes repeat enter money process
# if no return money


# Main()
