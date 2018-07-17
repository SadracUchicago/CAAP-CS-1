###Slope###
###By Jesus Almaraz Argueta###

#A function that sums a series of numbers entered by the user.

def slope():
  val = 0
  series_length = int(input('How many numbers are in the series:\n>>'))
  for i in range(series_length):
    if (i == 0):
      series_term = float(input('\nPlease enter the first term of the series:\n>>'))
    elif (i == (series_length - 1)):
      series_term = float(input('\nPlease enter the last term of the series:\n>>'))
    else:
      series_term = float(input('\nPlease enter the following term of the series:\n>>'))
    val += series_term
  print('\nThe sum of the series is: ' + str(int(val)))