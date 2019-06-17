# # Importing JSON File with vending machine items and price
# import json

# with open('items.json', 'r') as itemData:
#     data = itemData.read()

# obj = json.loads(data)


# function checking if user input is valid
# options: array of possible choices
# question: string of question that is asked
def inputCheck(question, options):

    user_input = input(question)

    while (user_input not in options):
        print("That is not a valid input.")
        user_input = input(question)

    return user_input


class VendingMachine:

    # example list of items
    item_choices = {"cookies": 0.50, "coke": 0.50,
                    "gatorade": 1.00, "candy": 0.10}
    # user's credit value
    user_credit = 0
    # user's item cost
    user_item_cost = 0
    # user balance due
    user_money_due = 0
    # user item choice
    user_item_choice = ""

    # constructor
    def __init__(self):
        pass

    ### INTRO PROCESS ###
    def intro(self):
        # list option of items user can purchase and price (from json file)
        # welcome prompt
        welcome_prompt = "Welcome to Dennis's Vending Machine! \n"
        print(welcome_prompt)
        print("Our items include: ")
        for key in self.item_choices.keys():
            print(key + " ${:0.2f}".format(self.item_choices[key]))

    ### ITEM CHOOSING PROCESS ###
    def itemChoosing(self):

        # ask user to choose which item they want
        pickItemQuestion = "\nWhat item would you like? "
        itemOptions = self.item_choices.keys()

        self.user_item_choice = inputCheck(pickItemQuestion, itemOptions)
        self.user_item_cost = self.item_choices.get(self.user_item_choice)

        # Why is print statement default to 2 lines when ctrl + s?
        # How to display 2 decimal places for cost?
        print("\nOk you have selected " + self.user_item_choice + ".")
        print("That will cost ${:0.2f}\n".format(self.user_item_cost))

        if (self.user_credit >= self.user_item_cost):
            self.checkEnoughMoney()
        else:
            self.payment()

        return self.user_item_cost

    ### PAYMENT PROCESS ###

    def payment(self):

        # hashmap of payment options
        paymentOptions = {'n': 0.05, 'd': 0.10, 'q': 0.25, 'b': 1.00}

        # list payment options to user
        pay_options_prompt = "Please pay by inserting the following 'n' = $0.05, 'd' = $0.10, 'q' = $0.25, 'b' = $1.00 \n"

        # ask user to enter money
        inserted_money = inputCheck(pay_options_prompt, paymentOptions.keys())

        # update user's credit and amount left due
        self.user_credit += paymentOptions.get(inserted_money)
        self.user_money_due = self.user_item_cost - self.user_credit

        # ask if user wants to insert more money
        if (self.user_money_due > 0):
            print("You have ${:0.2f}".format(
                self.user_money_due) + " left to pay.\n")
            self.askInsertMore()
        else:
            self.askInsertMore()

    # Asks user if they want to insert more money
    def askInsertMore(self):

        insertMoreQuestion = "Would you like to insert more money? 'y' = yes, 'n' = no \n"
        insertMoreOptions = ['y', 'n']

        insertMoreYN = inputCheck(insertMoreQuestion, insertMoreOptions)

        if (insertMoreYN == 'y'):
            self.payment()
        else:  # insertMoreYN == 'n'
            self.checkEnoughMoney()

    # checks if user's entered money is enough to buy chosen item
    def checkEnoughMoney(self):

        # TRANSACTION STEP
        # User has inserted enough money
        if (self.user_money_due <= 0):

            # subtract item cost from credit
            self.user_credit -= self.user_item_cost

            # give user their item
            print("Here is your " + self.user_item_choice)
            print("You have ${:0.2f}".format(self.user_credit) + " left.")

            # ask user if they want to buy more?
            if (self.askBuyMore()):
                self.itemChoosing()
            else:
                self.returnChange()

        else:
            print("You have inserted enough money.")
            self.askInsertMore()

    def askBuyMore(self):

        # Ask user if they want to buy more
        buyMoreQuestion = "Would you like to buy another item? 'y' or 'n' \n"
        buyMoreResponses = ['y', 'n']
        buyMoreYN = inputCheck(buyMoreQuestion, buyMoreResponses)

        if (buyMoreYN):
            return True
        else:
            return False

    # return change
    def returnChange(self):

        # thank you prompt
        thankyou_prompt = "Thank you for visiting Dennis's Vending Machine! Come again."

        print("Your change is ${:0.2}".format(self.user_credit))
        print(thankyou_prompt)


# main
machine1 = VendingMachine()
machine1.intro()
machine1.itemChoosing()
