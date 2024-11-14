import pytest
import pandas as pd
import sys
import os
from Script import calculate_sum, calculate_average, calculate_median, calculate_std_dev, calculate_linear_trend

# Sample data for testing
test_data = pd.DataFrame({
    'TAVG': [1, 2, 3, 4, 5]
})

# Test for sum calculation
def test_calculate_sum():
    result = calculate_sum(test_data['TAVG'])
    assert result == 15, f"Expected 15 but got {result}"

# Test for average calculation
def test_calculate_average():
    result = calculate_average(test_data['TAVG'])
    assert result == 3.0, f"Expected 3.0 but got {result}"

# Test for median calculation
def test_calculate_median():
    result = calculate_median(test_data['TAVG'])
    assert result == 3, f"Expected 3 but got {result}"

# Test for standard deviation calculation
def test_calculate_std_dev():
    result = calculate_std_dev(test_data['TAVG'])
    assert result == 1.58, f"Expected 1.58 but got {result}"

# Test for linear trend calculation
def test_calculate_linear_trend():
    result = calculate_linear_trend(test_data['TAVG'])
    assert result == 1.0, f"Expected 1.0 but got {result}"
