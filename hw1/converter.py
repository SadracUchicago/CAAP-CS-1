###Hello World###
###By Jesus Almaraz Argueta###

#A set of functions used to convert C-degrees to F-degrees and furlongs to meters

def cel_fah_con(): #C-deg to F-deg converter
  d_input, loop = 0, 1
  print('Fahrenheit to Celsius:[1]    Celsius to Fahrenheit:[2]\nQuit:[3]')
  while (loop == 1):
    d_input = int(input('\n>>'))
    if (d_input == 1):
      d_input = float(input('\nDegrees in Fahrenheit:\n>>'))
      for i in range(0, 6):
        print('Degrees in Celsius: ' + str((d_input - 32) * (5/9)))
    elif (d_input == 2):
      d_input = float(input('\nDegrees in Celsius:\n>>'))
      print('Degrees in Fahrenheit: ' + str((d_input * (9/5)) + 32))
    elif (d_input == 3):
      loop = 0
    else:
      print('\nERROR: Invalid input, please try again.')

def fur_met_con(): #Furlong to metric converter
  d_input, loop = 0, 1
  print('A furlong is an old English unit used to measure length.  It was based on the average length of a plowed furlow.  A furlong is equivalent to an eight of a mile, or 220 yards.  This program can be used to convert furlongs to meters/kilometers and vice versa.\n')
  print('Furlongs to Kilometers:[1]    Furlongs to Meters:[2]\nKilometers to Furlongs:[3]   Meters to Furlongs:[4]\nQuit:[5]')
  while (loop == 1):
    d_input = int(input('\n>>'))
    if (d_input == 1):
      d_input = float(input('\nLength in Furlongs:\n>>'))
      print('Length in Kilometers: ' + str((d_input * 201.168) / 1000))
    elif (d_input == 2):
      d_input = float(input('\nLength in Furlongs:\n>>'))
      print('Length in Meters: ' + str(d_input * 201.16))
    elif (d_input == 3):
      d_input = float(input('\nLength in Kilometers:\n>>'))
      print('Length in Furlongs: ' + str((d_input * 1000) / 201.16))
    elif (d_input == 4):
      d_input = float(input('\nLength in Meters:\n>>'))
      print('Length in Furlongs: ' + str(d_input / 201.16))
    elif (d_input == 5):
      loop = 0
    else:
      print('\nERROR: Invalid input, please try again.')