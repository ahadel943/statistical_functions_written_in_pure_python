# Statistical Function written in python

# Minimum Value => is the smallest number in an array
def minimum_value(arr):
  min_num = arr[0]
  for num in arr:
    if num < min_num:
      min_num = num
  return "Minimum Value: " + str(min_num)

arr = [2, 1, 5, 3, 4, 10, 60, 87]
print (minimum_value(arr))