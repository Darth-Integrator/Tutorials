# Function to calculate the mean of the array
def calculate_mean(arrayNumbers):
  sumNumbers = 0
  sizeArray = len(arrayNumbers)
  # arrayNumbers = 5
  for value in range(sizeArray):
    #sumNumbers = sumNumbers + arrayNumbers[value]
    sumNumbers += arrayNumbers[value]
  return sumNumbers/sizeArray

# You can use this to test your function.
# Any code inside this if statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your calculate_mean function with examples:
  mean = calculate_mean([1,2.2,0.3,3.4,7.9])
  print(mean)

  arrayName = "Ananth"
  # ["A", "n", "a", "n", "t", "h"]
  arrayName[2]