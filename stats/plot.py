import numpy as np
import matplotlib.pyplot as plt


# Круговая диаграмма
def piecat(values, labels):
    plt.pie(values, labels=labels, autopct='%1.f%%')
    plt.title('Распределение расходов по категориям')
    plt.show()


# Cтолбчатая диаграмма 
def barcat(values, labels):
    plt.bar(labels, values, color='orange', width=0.5)
    plt.xlabel('Категория')
    plt.ylabel('Сумма')
    plt.title('Общие расходы по категориям')
    plt.show()


# Гистограмма
def histcat(values):
    plt.hist(values, bins='auto', color='red', alpha=0.75)
    plt.xlabel('Сумма')
    plt.ylabel('Количество')
    plt.title('Распределение всех расходов')
    plt.show()


# Линейный график
def linecat(values):
    days = list(range(1, len(values) + 1))
    plt.plot(days, values, color='blue')
    plt.xlabel('День')
    plt.ylabel('Сумма')
    plt.title('Расходы по дням')
    plt.show()
