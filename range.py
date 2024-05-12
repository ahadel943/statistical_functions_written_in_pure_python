# Statistical Function written in python

def range(arr):
    # Check if the dataset is empty
    if not arr:
        return None
    # Find the minimum and maximum values
    min_value = arr[0]
    max_value = arr[0]
    for value in arr:
        if value < min_value:
            min_value = value
        elif value > max_value:
            max_value = value
    # Calculate the range
    range = max_value - min_value
    return range

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 16]
print(range(arr))