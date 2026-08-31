values = [10, 15, 20, 20, 25, 30, 100]


def mean(values):
    return sum(values) / len(values)


def median(values):
    values = sorted(values)

    if len(values) % 2 != 0:
        return values[len(values) // 2]
    else:
        return (values[len(values) // 2 - 1] + values[len(values) // 2]) / 2

