# Statistical Function written in python

# Mean => A function calculate the average value of a given data series
def mean(arr):
  arr_sum = 0
  for n in arr:
    arr_sum += n
  avg = arr_sum / len(arr)
  return "Mean is: " + str(avg)

arr = [2, 1, 5, 3, 4, 10, 60, 87]
print (mean(arr))