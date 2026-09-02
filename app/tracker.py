from stats.defstatistics import mean, median, minimum, maximum, std
from stats.plot import piecat, barcat, histcat, linecat


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
        return [expense for expense in self.expenses if expense.category.lower() == category.lower()]


def print_menu():
    print()
    print('=== Трекер Расходов ===\n\n1. Добавить расход\n2. Показать все расходы\n3. Показать общую сумму расходов\n4. Показать расходы по категории\n5. Статистика расходов\n6. Визуализация расходов\n7. Выйти')


def parse_amount(amount_str):
    if "." in amount_str or "," in amount_str:
        return float(amount_str.replace(",", "."))
    return int(amount_str)


def handle_add_expense(tracker):
    name = input('Название: ').strip()

    while True:
        amount_str = input('Сумма: ').strip()
        try:
            amount = parse_amount(amount_str)
            if amount <= 0:
                print('Сумма должна быть положительным числом. Попробуйте снова')
                continue
            break
        except ValueError:
            print('Некорректный ввод. Введите число, например 250 или 250.50')

    category = input('Категория: ').strip()

    tracker.add_expense(name, amount, category)
    print('\nРасход добавлен\n')


def handle_show_all(tracker):
    expenses = tracker.get_all_expenses()

    if not expenses:
        print('Список расходов пуст\n')
        return

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense}")
    print()    


def handle_show_total(tracker):
    print(f'Total: {tracker.get_total_expenses()}')


def handle_filter_by_category(tracker):
    expenses = tracker.get_all_expenses()

    if not expenses:
        print('Список расходов пуст — категорий пока нет.\n')
        return

    categories = sorted(set(expense.category.lower() for expense in expenses))
    print('Доступные категории:', ', '.join(categories))

    category = input('Введите категорию: ').strip()
    found = tracker.filter_by_category(category)

    if not found:
        print(f"Расходов в категории '{category}' не найдено\n")
        return

    for expense in found:
        print(f"{expense.name} - {expense.amount}")
    print()


def handle_show_statistics(tracker):
    expenses = tracker.get_all_expenses()

    if not expenses:
        print('Список расходов пуст\n')
        return

    amounts = [expense.amount for expense in expenses]

    print(f'Средний расход: {mean(amounts):.1f}')
    print(f'Медианный расход: {median(amounts)}')
    print(f'Минимальный расход: {minimum(amounts)}')
    print(f'Максимальный расход: {maximum(amounts)}')
    print(f'Стандартное отклонение: {std(amounts):.1f}\n')


def get_category_totals(tracker):
    expenses = tracker.get_all_expenses()
    totals = {}
    for expense in expenses:
        category = expense.category.lower()
        totals[category] = totals.get(category, 0) + expense.amount
    return totals

def print_visualization_menu():
    print('=== Визуализация Расходов ===\n\n1. Круговая диаграмма по категориям\n2. Столбчатая диаграмма по категориям\n3. Гистограмма распределения всех расходов\n4. Линейный график расхходов по дням\n5. Назад')


def handle_visualization(tracker):
    expenses = tracker.get_all_expenses()

    if not expenses:
        print('Список расходов пуст — нечего визуализировать.\n')
        return

    while True:
        print_visualization_menu()
        print()
        choice = input('Выберите график: ').strip()
        print()

        if choice == '1':
            totals = get_category_totals(tracker)
            piecat(list(totals.values()), list(totals.keys()))

        elif choice == '2':
            totals = get_category_totals(tracker)
            barcat(list(totals.values()), list(totals.keys()))

        elif choice == '3':
            amounts = [expense.amount for expense in expenses]
            histcat(amounts)

        elif choice == '4':
            amounts = [expense.amount for expense in expenses]
            linecat(amounts)

        elif choice == '5':
            break

        else:
            print('Введите число от 1 до 5\n')


def main():
    tracker = ExpenseTracker()
 
    while True:
        print_menu()
        print()
        choice = input('Выберите действие: ').strip()
        print()
    
        if choice == '1':
            handle_add_expense(tracker)
    
        elif choice == '2':
            handle_show_all(tracker)
    
        elif choice == '3':
            handle_show_total(tracker)
    
        elif choice == '4':
            handle_filter_by_category(tracker)

        elif choice == '5':
            handle_show_statistics(tracker)

        elif choice == '6':
            handle_visualization(tracker)

        elif choice == '7':
            print("Выход из программы")
            break

        else:
            print("Введите число от 1 до 7\n")

if __name__ == "__main__":
    main()        