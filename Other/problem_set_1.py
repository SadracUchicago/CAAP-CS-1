###CAAP CS 2018###
###Problem 1###
print('Problem #1')
def temp_convert():
	base = input('Please input the base:\n>> ')
	expnt = input('Please input the exponent:\n>> ')
	# HERE THE ISSUE IS THAT INPUT GETS STRINGS INSTEAD OF INTS. TRY TO PUT THE INPUT INSIDE int() TO CAST IT TO AN INT.
	print(str(base) + ' to the power of ' + str(expnt) + ' is ' + str(base ** expnt))
#temp_convert()

###Problem 2###
print('\nProblem #2')
def parall(): #This won't be the most efficient method to solve this problem....
	
	#There are multiple border cases this won't account for
	###Inputs###

	#AGAIN, USE int() TO TAKE IN NUMBER VALUES

	sideA = input('Please input the lenght of side A:\n>> ') #I realize now I could have condeced using simultaneous assignment
	sideB = input('Please input the lenght of side B:\n>> ')
	sideC = input('Please input the length of side c:\n>> ')
	sideD = input('Please input the length of side D:\n>> ')
	angleAB = input('Please input the degrees of angle AB:\n>> ')
	angleBC = input('Please input the degrees of angle BC:\n>> ')
	angleCD = input('Please input the degrees of angle CD:\n>> ')
	angleDA = input('Please input the degrees of angle DA:\n>> ')
	
	###Square/Rectangle###

	# IF STATEMENTS TAKE ONLY ONE 'CONDITION', SO IF YOU HAVE DIFFERENT CONDITIONS
	# YOU HAVE TO MAKE SURE THEY ARE ENCAPSULATED INTO ONE WITH PARENTHESIS

	if (angleAB == 90) and (angleBC == 90) and (angleCD == 90) and (angleDA == 90) and ((angleAB + angleBC + angleCD + angleDA) == 360):
		if (sideA == sideB) and (sideB == sideC) and (sideC == sideD) and (sideD == sideA):
			print('The given parameters indicate the figure is a square.')
		else:
			print('The given parameters indicate the figure is a rectangle.')
	###Rhombus/Parallelogram###
	elif (angleAB != 90) and (angleBC != 90) and (angleCD != 90) and (angleDA != 90) and ((angleAB + angleBC + angleCD + angleDA) == 360):
		if (sideA == sideB) and (sideB == sideC) and (sideC == sideD) and (sideD == sideA):
			print('The given parameters indicate the figure is a rhombus.')
		elif (angleAB == angleCD) or (angleBC == angleDA):
			print('The given parameters indicate the figure is a parallelogram.')
	###Trapezoid###
	elif (angleAB + angleBC + angleCD + angleDA) == 360:
		print('The given parameters indicate the figure is either a trapezoid or kite.')
	###Error###
	else:
		print('ERROR: Figure is impossible')
#parall()

###Problem 3###
print('\nProblem #3')
# Used these websites as reference:
# https://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.arccos.html
# https://docs.scipy.org/doc/numpy-1.10.4/reference/generated/numpy.rad2deg.html
def trgle():	

	# NUMPY IS A PYTHON LIBRARY WHICH YOU NEED TO INSTALL BEFORE YOU CAN USE IT
	# PUT THIS IN YOUR TERMINAL: pip install numpy
	# THIS SHOULD INSTALL THE PACKAGE AND YOU SHOULD BE ABLE TO USE IT THEN.

	import numpy as np
	
	###Inputs###
	sideA = float(input('Please input the lenght of side A:\n>> '))
	sideB = float(input('Please input the lenght of side B:\n>> '))
	sideC = float(input('Please input the length of side c:\n>> '))
	
	###Calculation of Angles###
	angleAB = np.rad2deg(np.arccos((sideC**2 - sideA**2 - sideB**2)/(-2 * sideA * sideB)))
	angleBC = np.rad2deg(np.arccos((sideA**2 - sideB**2 - sideC**2)/(-2 * sideB * sideC)))
	angleCA = np.rad2deg(np.arccos((sideB**2 - sideC**2 - sideA**2)/(-2 * sideC * sideA)))
	
	###Equilateral###
	if (sideA == sideB) and (sideB == sideC) and (sideC == sideA) and (angleAB == angleBC) and (angleBC == angleCA) and (angleCA == angleAB) and ((angleAB + angleBC + angleCA) == 180):
		print('The given parameters indicate the figure is an equilateral triangle.')
	###Isoceles###
	elif (sideA == sideB) or (sideB == sideC) or (sideC == sideA) and ((angleAB + angleBC + angleCA) == 180):
		if (angleAB > 90) or (angleBC > 90) or (angleCA > 90):
			print('The given parameters indicate the figure is an obtuse isoceles triangle.')
		elif (angleAB == 90) or (angleBC == 90) or (angleCA == 90):
			print('The given parameters indicate the figure is a right isoceles triangle.')
	###Scalene###
	elif (sideA != sideB) and (sideB != sideC) and (sideC != sideA) and ((angleAB + angleBC + angleCA) == 180):
		if (angleAB > 90) or (angleBC > 90) or (angleCA > 90):
			print('The given parameters indicate the figure is an obtuse scalene triangle.')
		elif (angleAB == 90) or (angleBC == 90) or (angleCA == 90):
			print('The given parameters indicate the figure is a right scalene triangle.')
		elif (angleAB < 90) and (angleBC < 90) and (angleCA < 90):
			print('The given parameters indicate the figure is an acute scalene triangle.')
	###Error###
	else:
		print('ERROR: Figure is impossible')
trgle()
