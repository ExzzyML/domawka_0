values = [10, 15, 20, 20, 25, 30, 100]


# Среднее значение
def mean(values):
    return sum(values) / len(values)


# Медиана
def median(values):
    values = sorted(values)

    if len(values) % 2 != 0:
        return values[len(values) // 2]

    else:
        return (values[len(values) // 2 - 1] + values[len(values) // 2]) / 2


# Дисперсия
def variance(values): 
    var = []

    for i in range(len(values)):
        var.append((values[i] - mean(values)) ** 2)

    return sum(var) / (len(values) - 1)


# Стандартное отклонение
def std(values):
    return variance(values) ** 0.5


# Минимум
def minimum(values):
    return min(values)


# Максимум
def maximum(values):
    return max(values)


# Квантиль
def quantile(values, q):
    values = sorted(values)
    n = len(values)
    position = n * q

    if position == int(position):
        return values[int(position) - 1]  
      
    else:
        lower_index = int(position)
        upper_index = lower_index + 1
        lower_value = values[lower_index - 1]
        upper_value = values[upper_index - 1]
        return (lower_value + upper_value) / 2


# Межквартильный размах
def data_range(values):
    return (quantile(values, 0.75) - quantile(values, 0.25))    