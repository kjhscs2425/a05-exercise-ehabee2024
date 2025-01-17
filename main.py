
"""
`check_fever` should return `True` if the temperature is `100.4` or higher. For
any lower temperature, it should return `False`.
"""
def check_fever(temperature):
  #YOUR CODE HERE
  return

# Get temperature from user and convert to float
temp = ...
if check_fever(100):
  print("You have a fever.")
else:
  print("You don't have a fever.")





  # Function to check if the temperature indicates a fever
def check_fever(temp):
    return temp >= 100.4

# Get temperature from user and convert to float
temp = float(input("Enter your temperature: "))

# Check if the person has a fever
if check_fever(temp):
    print("You have a fever.")
else:
    print("You don't have a fever.")