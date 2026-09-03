# Expense Tracker

## Что делает приложение

Expense Tracker — консольное приложение для учёта личных расходов. Позволяет добавлять расходы с указанием названия, суммы и категории, просматривать список всех расходов, считать общую сумму, фильтровать по категории, а также получать статистику (среднее, медиану, минимум, максимум, стандартное отклонение) и визуализировать расходы в виде круговой диаграммы, столбчатой диаграммы, гистограммы и линейного графика.

## Как установить проект

```bash
git clone https://github.com/ExzzyML/domawka_0.git
cd domawka_0
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Как запустить

```bash
python -m app.tracker
```

## Как запустить тесты

```bash
python -m pytest
```

## Структура проекта

domawka_0/
├── app/
│   ├── __init__.py
│   └── tracker.py          # консольное приложение Expense Tracker: классы Expense, ExpenseTracker, меню
├── stats/
│   ├── __init__.py
│   ├── defstatistics.py    # функции статистики: mean, median, variance, std, minimum, maximum, quantile, data_range
│   └── plot.py              # функции визуализации: piecat, barcat, histcat, linecat
├── tests/
│   ├── test_statistics.py  # тесты для функций из stats/defstatistics.py
│   └── test_tracker.py     # тесты для Expense и ExpenseTracker
├── .gitignore
├── requirements.txt
└── README.md
