# Statistical Function written in python

# Median => A function calculate the middle value of a given data series
def median(arr):
    sorted_data = sorted(arr)
    n = len(sorted_data)
    if n % 2 == 0:
        # If the number of elements is even, take the average of the middle two elements
        middle_left = sorted_data[n // 2 - 1]
        middle_right = sorted_data[n // 2]
        median = (middle_left + middle_right) / 2
    else:
        # If the number of elements is odd, take the middle element
        median = sorted_data[n // 2]
    return median

arr = [2, 1, 5, 3, 4, 10, 60, 87]
print(median(arr))