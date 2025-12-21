class Category:
    def __init__ (self,name):
        self.name = name
        self.ledger = []

    #deposit to instance add entry
    def deposit(self,amount,description=""):
        #check for funds
        self.check_funds(amount)
            
        self.ledger.append({
                "amount": amount,
                "description": description
                })
        
    #withdraw balance and add entry
    def withdraw(self,amount,description=""):
        #check for funds first
        if not self.check_funds(amount):
            return False
        self.ledger.append({
            "amount": -amount,
            "description": description
        })
        return True 
    
    #get balance from instance
    def get_balance(self):
        result = 0
        for item in self.ledger:
            result = result + item["amount"]
        return result

    #transfer funds from one instance to another
    def transfer(self,amount,destination):
        if self.withdraw(amount,f"Transfer to {destination.name}"):
            destination.deposit(amount,f"Transfer from {self.name}")
            return True
        return False

    #check sufficent funds
    def check_funds(self,amount):
        if self.get_balance() < amount:
            return False
        return True

    #output
    def __str__ (self):
        output = self.name.center(30,"*") +"\n"

        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            output += desc + amt + "\n"

        output += f"Total: {self.get_balance():.2f}"
        return output



def create_spend_chart(categories):
    spent = [] #emptu list to store total money spent

    # Calculate total spent per category
    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        spent.append(total)

    total_spent = sum(spent)

    # Convert to percentages (rounded down to nearest 10)
    percentages = []
    for spent_amount in spent:
        #convert spending to %
        percent = (spent_amount / total_spent) * 100
        #rount down to nearest 10 
        percent = int(percent // 10) * 10
        percentages.append(percent)

    chart = "Percentage spent by category\n"

    # Build percentage chart
    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += f"{str(i).rjust(3)}|"
        for percent in percentages:
            if percent >= i:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"


    # Horizontal line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"



    # Category names vertically
    max_len = max(len(cat.name) for cat in categories)

    for i in range(max_len):
        chart += "     "
        for cat in categories:
            chart += (cat.name[i] if i < len(cat.name) else " ") + "  "
        chart += "\n"

    return chart.rstrip("\n")



food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
slots = Category("Slots")
slots.deposit(500, "egt")
print(clothing)
print(food)
print(create_spend_chart([food,clothing,slots]))