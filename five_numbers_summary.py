# Statistical Function written in python

# The five-number summary => is a descriptive statistics technique used to summarize the distribution of a dataset
def five_number_summary(data):
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    minimum = sorted_data[0]
    maximum = sorted_data[-1]
    
    median = sorted_data[n // 2] if n % 2 != 0 else (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    
    lower_half = sorted_data[:n // 2]
    upper_half = sorted_data[n // 2 + n % 2:]
    
    q1 = lower_half[len(lower_half) // 2] if len(lower_half) % 2 != 0 else (lower_half[len(lower_half) // 2 - 1] + lower_half[len(lower_half) // 2]) / 2
    q3 = upper_half[len(upper_half) // 2] if len(upper_half) % 2 != 0 else (upper_half[len(upper_half) // 2 - 1] + upper_half[len(upper_half) // 2]) / 2
    
    return minimum, q1, median, q3, maximum

data = [12, 45, 7, 23, 56, 19, 8, 35, 62]
min_val, q1_val, median_val, q3_val, max_val = five_number_summary(data)
print("Minimum:", min_val)
print("First Quartile (Q1):", q1_val)
print("Median (Q2):", median_val)
print("Third Quartile (Q3):", q3_val)
print("Maximum:", max_val)
