import pytest
from app.tracker import Expense, ExpenseTracker


# expense

def test_expense_creation():
    expense = Expense("Coffee", 250, "food")
    assert expense.name == "Coffee"
    assert expense.amount == 250
    assert expense.category == "food"


def test_expense_str():
    expense = Expense("Coffee", 250, "food")
    assert str(expense) == "Coffee - 250 - food"


# add_expense / get_all_expenses 

def test_add_expense():
    tracker = ExpenseTracker()
    tracker.add_expense("Coffee", 250, "food")

    expenses = tracker.get_all_expenses()
    assert len(expenses) == 1
    assert expenses[0].name == "Coffee"
    assert expenses[0].amount == 250
    assert expenses[0].category == "food"


def test_add_multiple_expenses():
    tracker = ExpenseTracker()
    tracker.add_expense("Coffee", 250, "food")
    tracker.add_expense("Taxi", 800, "transport")

    expenses = tracker.get_all_expenses()
    assert len(expenses) == 2


def test_get_all_expenses_empty():
    tracker = ExpenseTracker()
    assert tracker.get_all_expenses() == []


# get_total_expenses

def test_get_total_expenses():
    tracker = ExpenseTracker()
    tracker.add_expense("Coffee", 100, "food")
    tracker.add_expense("Taxi", 500, "transport")

    assert tracker.get_total_expenses() == 600


def test_get_total_expenses_empty():
    tracker = ExpenseTracker()
    assert tracker.get_total_expenses() == 0


def test_get_total_expenses_single():
    tracker = ExpenseTracker()
    tracker.add_expense("Coffee", 250, "food")
    assert tracker.get_total_expenses() == 250


# filter_by_category

def test_filter_by_category_basic():
    tracker = ExpenseTracker()
    tracker.add_expense("Coffee", 250, "food")
    tracker.add_expense("Taxi", 800, "transport")
    tracker.add_expense("Burger", 650, "food")

    found = tracker.filter_by_category("food")
    assert len(found) == 2
    assert all(expense.category == "food" for expense in found)


def test_filter_by_category_case_insensitive():
    tracker = ExpenseTracker()
    tracker.add_expense("Coffee", 250, "Food")

    found = tracker.filter_by_category("food")
    assert len(found) == 1
    assert found[0].name == "Coffee"


def test_filter_by_category_not_found():
    tracker = ExpenseTracker()
    tracker.add_expense("Coffee", 250, "food")

    found = tracker.filter_by_category("transport")
    assert found == []


def test_filter_by_category_empty_tracker():
    tracker = ExpenseTracker()
    found = tracker.filter_by_category("food")
    assert found == []