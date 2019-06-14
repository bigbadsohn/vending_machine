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

    options.lower()

    user_input = input(question)
    user_input.lower()

    while (user_input not in options):
        user_input = input(question)


#make a vending machine class?

### BOOKEND PROMPTS ###
# welcome prompt
welcome_prompt = "Welcome to Dennis's Vending Machine \n"
# thank you prompt
thankyou_prompt = "Thank you for visiting Dennis's Vending Machine! Come again."

# list option of items user can purchase and price (from json file)


### BUYING PROCESS ###
# ask user to choose which item they want



### PAYMENT PROCESS ###

# list payment options to user
pay_options_prompt = "Please pay with following 'n' = $0.05, 'd' = $0.10, 'q' = $0.25, 'b' = $1.00 \n"
# hashmap of payment options
paymentOptions = {'n': 0.05, 'd': 0.10, 'q': 0.25, 'b': 1.00}

# ask user to enter money


# check if user inserted enough money for item


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
