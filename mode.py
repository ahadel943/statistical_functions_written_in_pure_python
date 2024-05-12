# Statistical Function written in python

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
  
data = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7]
print("Mode:", mode(data))