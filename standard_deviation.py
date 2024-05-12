# Statistical Function written in python

# Standard Deviation => is a measure of dispersion or spread in a data.
def calculate_mean(data):
    """Calculate the mean of a list of numbers."""
    n = len(data)
    if n < 1:
        raise ValueError('Mean cannot be calculated for empty data')
    return sum(data) / n

def calculate_variance(data):
    """Calculate the variance of a list of numbers."""
    n = len(data)
    if n < 2:
        raise ValueError('Variance cannot be calculated with less than 2 data points')
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / (n - 1)

def calculate_standard_deviation(data):
    """Calculate the standard deviation of a list of numbers."""
    variance = calculate_variance(data)
    return variance ** 0.5

# Example usage:
data = [5, 10, 15, 20, 25]
std_deviation = calculate_standard_deviation(data)
print("Standard Deviation:", format(std_deviation, '.2f'))
