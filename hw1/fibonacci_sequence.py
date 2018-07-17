###Fibonacci Sequence###
###By Jesus Almaraz Argueta###

#A function to calculate the nth term of the Fibonacci Sequence.

def fib_seq():
  val_n_1, val_n_2, val_n = 0, 1, 0
  term_n = int(input('Please enter to which term you would like to calculate the Fibonacci Sequence:\n>>'))
  for i in range(term_n):
    val_n = val_n_1 + val_n_2
    val_n_1, val_n_2 = val_n, val_n_1
  print('\nThe value of the Fibonacci Sequence at term n=' + str(term_n) + ' is: ' + str(val_n))