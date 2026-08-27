# God bless me 

class Expense:

    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

    def __str__(self):
        return f"{self.name} - {self.amount} - {self.category}"


class ExpenseTracker:

    def __init__(self):
        self.expenses = []

    def add_expense(self, name, amount, category):
        expense = Expense(name, amount, category)
        self.expenses.append(expense)

    def get_all_expenses(self):
        return self.expenses

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def filter_by_category(self, category):
        return [expense for expense in self.expenses if expense.category == category]

    
