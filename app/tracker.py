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


def main():
    tracker = ExpenseTracker()
 
    while True:
        print('=== Expense Tracker ===\n1. Добавить расход\n2. Показать все расходы\n3. Показать общую сумму расходов\n4. Показать расходы по категории\n5. Выйти')
        choice = input('Выберите действие: ')
    
        if int(choice) == 1:
            name = input('Название расхода: ')
            amount = int(input('Сумма: '))
            category = input('Категория: ')
            tracker.add_expense(name, amount, category)
    
        elif int(choice) == 2:
            expenses_list = tracker.get_all_expenses()
            for index, expense in enumerate(expenses_list, start=1):
                print(f"{index}. {expense}")
    
        elif int(choice) == 3:
            print(f'Total: {tracker.get_total_expenses()}')
    
        elif int(choice) == 4:
            category = input('Какая категория? ')
            found = tracker.filter_by_category(category)
            for expense in found:
                print(f"{expense.name} - {expense.amount}")
    
        elif int(choice) == 5:
            break

if __name__ == "__main__":
    main()        