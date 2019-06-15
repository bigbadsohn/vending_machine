# Importing JSON File with vending machine items and price
import json

with open('items.json', 'r') as itemData:
    data = itemData.read()

obj = json.loads(data)


# test example hashmap of items
items = {"cookie": 1.00, "coke": 0.75, "candy": 0.50}


# function checking if user input is valid
# options: array of possible choices
# question: string of question that is asked
def inputCheck(question, options):

    user_input = input(question)

    while (user_input not in options):
        print("That is not a valid input.")
        user_input = input(question)

    return user_input


# example items list
items = {"cookies": 0.50, "coke": 0.50, "gatorade": 1.00, "candy": 0.10}


### GLOBAL PROMPTS ###
# welcome prompt
welcome_prompt = "Welcome to Dennis's Vending Machine \n"
# thank you prompt
thankyou_prompt = "Thank you for visiting Dennis's Vending Machine! Come again."


### INTRO PROCESS ###
# list option of items user can purchase and price (from json file)
print(welcome_prompt)
print("Our items include: ")
for key in items.keys():
    print(key)


### BUYING PROCESS ###
# ask user to choose which item they want
pickItemQuestion = "\nWhat item would you like? "
itemOptions = items.keys()

user_item_choice = inputCheck(pickItemQuestion, itemOptions)
user_item_cost = items.get(user_item_choice)

# Why is print statement default to 2 lines when ctrl + s?
# How to display 2 decimal places for cost?
print("Ok you have selected " + user_item_choice +
      ". Please pay $" + str(user_item_cost))


### PAYMENT PROCESS ###
# list payment options to user
pay_options_prompt = "Please pay with following 'n' = $0.05, 'd' = $0.10, 'q' = $0.25, 'b' = $1.00 \n"

# hashmap of payment options
paymentOptions = {'n': 0.05, 'd': 0.10, 'q': 0.25, 'b': 1.00}


# ask user to enter money
# inserted_money = inputCheck(pay_options_prompt, paymentOptions.items())


# check if user inserted enough money for item
user_money_credit = 0


### POST PROCESSING ###
# if yes, give item and ask if they want to buy something else with extra money
# if yes repeat process
# if no give user change

# if no, ask user to enter more money
def payMore():

    payMoreQuestion = "Would you like to insert more money? 'y' = yes, 'n' = no \n"
    payMoreOptions = ['y', 'n']

    userPayMore = inputCheck(payMoreQuestion, payMoreOptions)

    if (userPayMore == 'y'):
        # add payment function
        pass
    else:
        thankyou_prompt


# if yes repeat enter money process
# if no return money


# Main()
