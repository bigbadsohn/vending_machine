# # Importing JSON File with vending machine items and price
# import json

# with open('items.json', 'r') as itemData:
#     data = itemData.read()

# obj = json.loads(data)


### GLOBAL VARS AND PROMPTS ###
# example items list
item_list = {"cookies": 0.50, "coke": 0.50, "gatorade": 1.00, "candy": 0.10}

# user's credit value
user_credit = 0

# user's item cost
user_item_cost = 0

# user balance due
user_money_due = 0

# user item choice
user_item_choice = ""

# welcome prompt
welcome_prompt = "Welcome to Dennis's Vending Machine! \n"

# thank you prompt
thankyou_prompt = "Thank you for visiting Dennis's Vending Machine! Come again."


# function checking if user input is valid
# options: array of possible choices
# question: string of question that is asked
def inputCheck(question, options):

    user_input = input(question)

    while (user_input not in options):
        print("That is not a valid input.")
        user_input = input(question)

    return user_input

### INTRO PROCESS ###


def intro():
    # list option of items user can purchase and price (from json file)
    print(welcome_prompt)
    print("Our items include: ")
    for key in item_list.keys():
        print(key + " ${:0.2f}".format(item_list[key]))


### ITEM CHOOSING PROCESS ###
def itemChoosing():
    # ask user to choose which item they want
    pickItemQuestion = "\nWhat item would you like? "
    itemOptions = item_list.keys()

    user_item_choice = inputCheck(pickItemQuestion, itemOptions)
    user_item_cost = item_list.get(user_item_choice)

    # Why is print statement default to 2 lines when ctrl + s?
    # How to display 2 decimal places for cost?
    print("\nOk you have selected " + user_item_choice + ".")
    print("That will cost ${:0.2f}\n".format(user_item_cost))


### PAYMENT PROCESS ###

def payment():
    # hashmap of payment options
    paymentOptions = {'n': 0.05, 'd': 0.10, 'q': 0.25, 'b': 1.00}

    # list payment options to user
    pay_options_prompt = "Please pay by ihserting the following 'n' = $0.05, 'd' = $0.10, 'q' = $0.25, 'b' = $1.00 \n"

    # ask user to enter money
    inserted_money = inputCheck(pay_options_prompt, paymentOptions.keys())

    # update user's credit and amount left due
    user_credit += paymentOptions.get(inserted_money)
    user_money_due = user_item_cost - user_credit

    # ask if user wants to insert more money
    if (user_money_due > 0):
        print("You have $" + str(user_money_due) + " due.")
        askInsertMore()
    else:
        askInsertMore()


# Asks user if they want to insert more money
# either runs payment function again or returns false
def askInsertMore():

    insertMoreQuestion = "Would you like to insert more money? 'y' = yes, 'n' = no \n"
    insertMoreOptions = ['y', 'n']

    insertMoreChoice = inputCheck(insertMoreQuestion, insertMoreOptions)
    if (insertMoreChoice == 'y'):
        payment()
    else:
        # insertMoreChoice == 'n'
        return False


# checks if user's entered money is enough to buy chosen item
# happens when insert money returns false
def checkEnoughMoney():

    # user confirms they don't want to insert more money
    if (askInsertMore == False):

        # check if user has enough money for chosen item
        # if yes, give them item and subtract from their credit
        if (user_money_due <= 0):

            print("Here is your " + user_item_choice)

        # if no, ask if they want to insert more money

        # if no, return credit (change) and


def transactionProcess():
    pass

### POST PROCESSING ###
# if yes, give item and ask if they want to buy something else with extra money
# if yes repeat process
# if no give user change
# main


intro()
itemChoosing()
payment()
