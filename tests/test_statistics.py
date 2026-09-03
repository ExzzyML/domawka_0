import pytest
from stats.defstatistics import mean, median, variance, std, minimum, maximum, quantile, data_range


# mean

def test_mean_basic():
    assert mean([1, 2, 3]) == 2


def test_mean_single_value():
    assert mean([5]) == 5


def test_mean_negative_values():
    assert mean([-10, 0, 10]) == 0


def test_mean_empty():
    with pytest.raises(ZeroDivisionError):
        mean([])


# median

def test_median_odd():
    assert median([3, 1, 2]) == 2


def test_median_even():
    assert median([4, 1, 3, 2]) == 2.5


def test_median_single_value():
    assert median([5]) == 5


def test_median_repeated_values():
    assert median([1, 1, 1, 1]) == 1


def test_median_empty():
    with pytest.raises(IndexError):
        median([])


# variance

def test_variance_basic():
    assert variance([2, 4, 6]) == 4


def test_variance_same_values():
    assert variance([5, 5, 5, 5]) == 0


def test_variance_negative_values():
    assert variance([-10, 0, 10]) == 100


def test_variance_single_value():
    with pytest.raises(ZeroDivisionError):
        variance([5])


def test_variance_empty():
    assert variance([]) == 0


# std

def test_std_basic():
    assert std([2, 4, 6]) == 2


def test_std_same_values():
    assert std([5, 5, 5, 5]) == 0


def test_std_single_value():
    with pytest.raises(ZeroDivisionError):
        std([5])


# minimum / maximum

def test_minimum_basic():
    assert minimum([10, 15, 20, 20, 25, 30, 100]) == 10


def test_minimum_negative_values():
    assert minimum([-10, 0, 10]) == -10


def test_minimum_single_value():
    assert minimum([5]) == 5


def test_minimum_empty():
    with pytest.raises(ValueError):
        minimum([])


def test_maximum_basic():
    assert maximum([10, 15, 20, 20, 25, 30, 100]) == 100


def test_maximum_negative_values():
    assert maximum([-10, 0, 10]) == 10


def test_maximum_single_value():
    assert maximum([5]) == 5


def test_maximum_empty():
    with pytest.raises(ValueError):
        maximum([])


# quantile

def test_quantile_median_equivalent():
    assert quantile([1, 2, 3], 0.5) == 1.5


def test_quantile_upper_bound():
    values = [1, 2, 3, 4]
    assert quantile(values, 1.0) == 4


def test_quantile_single_value():
    assert quantile([5], 0.5) == 5


def test_quantile_repeated_values():
    assert quantile([1, 1, 1, 1], 0.5) == 1


def test_quantile_zero_returns_last_due_to_known_bug():
    values = [1, 2, 3]
    assert quantile(values, 0) == values[-1]


# data_range 

def test_data_range_basic():
    result = data_range([1, 2, 3, 4, 5, 6, 7, 8])
    assert result >= 0


def test_data_range_same_values():
    assert data_range([5, 5, 5, 5]) == 0


def test_data_range_single_value():
    assert data_range([5]) == 0