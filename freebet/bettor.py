class Bettor:
    
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

jon = Bettor(10)
print(jon.get_balance())