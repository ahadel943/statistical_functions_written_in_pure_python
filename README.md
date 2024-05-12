# Statistical Function written in pure python

## Minimum Value

A function to calculate the lowest recorded value in a data series.

```python
  def minimum_value(arr):
  min_num = arr[0]
  for num in arr:
    if num < min_num:
      min_num = num
  return "Minimum Value: " + str(min_num)
```

## Maximum Value

A function to calculate the highest recorded value in a data series.

```python
  def maximum_value(arr):
    max_num = arr[0]
    for num in arr:
      if num > max_num:
        max_num = num
    return "Maximum Value: " + str(max_num)
```

## Mean

A function to calculate the average/mean which is a measure of central tendency that represents the typical value of a dataset.

```python
  def mean(arr):
  arr_sum = 0
  for n in arr:
    arr_sum += n
  avg = arr_sum / len(arr)
  return "Mean is: " + str(avg)
```

## Median

 A function to calculate the median which is the middle value when the data points are arranged in ascending or descending order.

 ```python
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
 ```

## Standard Deviation

A function to calculate standard deviation which is a measure of the dispersion or spread of a set of values in a dataset

```python
  def calculate_mean(data):
    # Calculate the mean of a list of numbers.
    n = len(data)
    if n < 1:
        raise ValueError('Mean cannot be calculated for empty data')
    return sum(data) / n

  def calculate_variance(data):
      # Calculate the variance of a list of numbers.
      n = len(data)
      if n < 2:
          raise ValueError('Variance cannot be calculated with less than 2 data points')
      mean = calculate_mean(data)
      return sum((x - mean) ** 2 for x in data) / (n - 1)

  def calculate_standard_deviation(data):
      # Calculate the standard deviation of a list of numbers.
      variance = calculate_variance(data)
      return variance ** 0.5
```

## Five Numbers Summary

A function to calculate the five numbers summary which is a descriptive statistics technique used to summarize the distribution of a dataset.

```python
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
```

## Mode

A function to calculte the mode which is the value that appears most frequently in a dataset.

```python
  def mode(data):
  # Create a dictionary to store the frequency of each unique value
  freq_dict = {}
  # Iterate through the data and count the frequency of each value
  for value in data:
    freq_dict[value] = freq_dict.get(value, 0) + 1
  # Find the value with the highest frequency (mode)
  mode = max(freq_dict, key=freq_dict.get)
  # Check if there are multiple modes
  multiple_modes = [key for key, value in freq_dict.items() if value == freq_dict[mode]]
  if len(multiple_modes) > 1:
    return "Multiple modes: " + ", ".join(str(mode) for mode in multiple_modes)
  else:
    return mode
```

## Range

A function to calculate the rage which is the difference between the maximum and minimum values in a data series.

```python
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
```