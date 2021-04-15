class Budget:
    """
    this is a software that allows user to keep track of their expenditure and make transfer to the categories when
    they are on less fund
    """
    def __init__(self, **positions):
        self.positions = positions
        print(positions)

    def deposit(self, amount, position):
        self.positions[position] = self.positions[position] + amount
        print("You have made a deposit of $", str(amount), "to", position)

    def withdraw(self, amount, position):
        if amount > self.positions[position]:
            print("You are low on funds")
        else:
            self.positions[position] = self.positions[position] + amount
            print("You withdrew the sum  of $", str(amount), "from", position)

    def transfer(self, amount, lossposition, gainposition):
        if amount > self.positions[lossposition]:
            print('Insufficient Balance')
        else:
            self.positions[lossposition] = self.positions[lossposition] - amount
            self.positions[gainposition] = self.positions[gainposition] + amount
            print('You transferred the sum of $', str(amount), 'from ', lossposition, ' to ', gainposition)

    def checkBalance(self, position):
        print('Your ', position, ' budget balance is ', str(self.positions[position]))


customerBudget = Budget(food=100, clothing=200, rent=3000, entertainment=150)  # initial deposit of the user....

print(
    "what would you like to do?\n| | | |\n| | | |\n> > > >\n(1).Deposit\n(2).Withdraw\n(3).Transfer\n(4).Check "
    "Balance\n(5).Exit")

# get input from user to perform the following task

selected_choice = int(input("Enter your choice\n---> "))
if selected_choice == 1:
    amount = int(input("Enter amount\n---> "))
    print("""
        (1).Entertainment
        (2).Food
        (3).Clothing
        input any category to deposit....
        """)
    category = input("Enter the category ---> ").lower()

    customerBudget.deposit(amount, category)

elif selected_choice == 2:
    amount = int(input("Enter amount\n---> "))
    print("""
        (1).Entertainment
        (2).Food
        (3).Clothing
        input any category to withdraw....
        """)
    category = input("Enter the category ---> ").lower()

    customerBudget.withdraw(amount, category)

elif selected_choice == 3:
    amount = int(input("Enter amount\n---> "))
    print("""
        (1).Entertainment
        (2).Food
        (3).Clothing
        input 'The two category you like to make transfer' ....
        """)

    category1 = input("Enter the category to collect cash for transfer\n---> ").lower()
    category2 = input("Enter the category to send the transfer\n---> ").lower()

    customerBudget.transfer(amount, category1, category2)

elif selected_choice == 4:
    print("""
    (1).Entertainment
    (2).Food
    (3).Clothing
    input any category to get balance....
    """)
    category = input("Enter the category ---> ").lower()
    customerBudget.checkBalance(category)

elif selected_choice == 5:
    exit()

else:
    print("Invalid input")
