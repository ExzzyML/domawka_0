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
    plt.ylabel('Расходы')
    plt.title('Общие расходы по категориям')
    plt.show()


# Гистограмма
def histcat(values):
    plt.hist(values, bins='auto', color='red', alpha=0.75)
    plt.xlabel('Расходы')
    plt.ylabel('Количество')
    plt.title('Распределение всех расходов')
    plt.show()