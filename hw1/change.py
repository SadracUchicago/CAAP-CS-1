###Change Calculator###
###By Jesus Almaraz Argueta###

#A function that finds the smallest number of American bills and coins equal to an arbitrary dollar amount entered by the user.
#Used https://stackoverflow.com/questions/20457038/how-to-round-down-to-2-decimals-with-python as reference

def change():
  import math
  change, tender = round(float(input('Please input a dollar amount:\n>>')), 2), []
  for i in [100, 50, 20, 10, 5, 1, 0.25, 0.1, 0.05, 0.01]:
    tender.append(math.floor(change / i))
    change = round((change % i), 2)
  print('\nHundreds: ' + str(tender[0]) + '\nFifties: ' + str(tender[1]) + '\nTwenties: ' + str(tender[2]) + '\nTens: ' + str(tender[3]) + '\nFives: ' + str(tender[4]) + '\nOnes: ' + str(tender[5]) + '\nQuarters: ' + str(tender[6]) + '\nDimes: ' + str(tender[7]) + '\nNickels: ' + str(tender[8]) + '\nPennies: ' + str(tender[9]))