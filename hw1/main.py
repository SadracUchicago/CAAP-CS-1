###Assignment 1###
###By Jesus Almaraz Argueta###

#A program to run all the other programs from a single place
#Used this https://stackoverflow.com/questions/20309456/call-a-function-from-another-file-in-python as reference

#Importing my funtions
import change as chg
import converter as cov
import fibonacci_sequence as fib
import hello_world as hlwd
import slope as sl

#Variables
input_, loop = 0, 1

#Main loop
while (loop == 1):
  print('\n--------------------------------------------------\nAssignment 1:\nHello World:[1]   Celsius/Fahrenheit Converter:[2]\nFurlong/Meter/Kilometer Converter:[3]   Slope:[4]\nFibonacci Sequence:[5]   Change Calculator:[6]\nQuit:[7]\n--------------------------------------------------')
  input_ = int(input('>>'))
  if (input_ == 1):
    print('Running Hello World:\n')
    hlwd.hello_world()
  elif (input_ == 2):
    print('Running Celsius/Fahrenheit Converter:\n')
    cov.cel_fah_con()
  elif (input_ == 3):
    print('Running Furlong/Meter/Kilometer Converter:\n')
    cov.fur_met_con()
  elif (input_ == 4):
    print('Running Slope:\n')
    sl.slope()
  elif (input_ == 5):
    print('Running Fibonacci Sequence:\n')
    fib.fib_seq()
  elif (input_ == 6):
    print('Running Change Calculator:\n')
    chg.change()
  elif (input_ == 7):
    loop = 0
  else:
    print('\nERROR: Invalid input, please try again.')