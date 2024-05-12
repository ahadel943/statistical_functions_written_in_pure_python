# Statistical Function written in python

# Maximum Value => is the largest number in an array
def maximum_value(arr):
  max_num = arr[0]
  for num in arr:
    if num > max_num:
      max_num = num
  return "Maximum Value: " + str(max_num)

arr = [2, 1, 5, 3, 4, 10, 60, 87]
print (maximum_value(arr))