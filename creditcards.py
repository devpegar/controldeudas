class CreditCard:

    def __init__(self, id, name, deadline, duedate, balance):
        self.id = id
        self.name = name
        self.deadline = deadline
        self.duedate = duedate
        self.balance = balance

    def __str__(self):
        return '{}, {}, {}, {}, {}'.format(self.id, self.name, self.deadline, self.duedate, self.balance)

