# CAAP CS - Assignment 1

## Introduction
All of the Python files included as part of my response were created in Python 3.  In order to run the program, the user must able to run Python 3.  The answers to each problem are in separate files in order to make understanding the code easier.  All the files can be executed from the main.py file.  

NOTE: Individual files cannot be executed on their own.  File main.py is needed to run any other Python file included in this folder.

## File Descriptions
* main.py - A used program to run all the other programs from a single place.
* change.py - A function that finds the smallest number of American bills and coins equal to an arbitrary dollar amount entered by the user.
* converter.py - A set of functions used to convert C-degrees to F-degrees and furlongs to meters/kilometers and vice versa.
* fibonacci_sequence.py - A function to calculate the nth term of the Fibonacci Sequence.
* hello_world.py - A function that writes a short poem based on inputs given by the user.
* slope.py - A function that sums a series of numbers entered by the user.

## Running the Program

To run the program, first go to the directory in which the files are stored.  Then run the following command in the terminal:
```
python3 main.py
```
If the program is run successfully, you should see the following output:
```
--------------------------------------------------
Assignment 1:
Hello World:[1]   Celsius/Fahrenheit Converter:[2]
Furlong/Meter/Kilometer Converter:[3]   Slope:[4]
Fibonacci Sequence:[5]   Change Calculator:[6]
Quit:[7]
--------------------------------------------------
>> 
```
This menu is used to select the program you would like to run.  To execute a program, simply input the number in brackets next to the program name.

NOTE: Whenever the program requires an input, the following line will be displayed:
```
>>[INPUT]
```

### Hello World
The program will prompt you with the following output:
```
What is your name?
 >>[NAME]
What state are you from?
 >>[STATE]
What is your favorite color?
 >>[COLOR]
What are your prefered pronouns?
 >>[PRONOUNS]
```
For pronouns, the program supports "he" and "she," as well as "ze," "xe," "ey," "ne," and "they."  If the user enters an unsupported pronound the program defaults to "they."  Once the user has entered the required inputs, the program will return something similar to this:
```
I met a person, a nice person,
By the name of [NAME].
[COLOR] they, told me,
Was their favorite color.
Oh, from [STATE] they came.
```

### Celsius/Fahrenheit Converter
The program will prompt you with the following output:
```
Fahrenheit to Celsius:[1]    Celsius to Fahrenheit:[2]
Quit:[3]

>>
```
This is functionally identical to the menu prompt you see when you first run the program.

NOTE: This program will run until the user tells it to quit.

### Furlong/Meter/Kilometer Converter
The program will prompt you with the following output:
```
A furlong is an old English unit used to measure length.  It was based on the average length of a plowed furlow.  A furlong is equivalent to an eight of a mile, or 220 yards.  This program can be used to convert furlongs to meters/kilometers and vice versa.

Furlongs to Kilometers:[1]    Furlongs to Meters:[2]
Kilometers to Furlongs:[3]   Meters to Furlongs:[4]
Quit:[5]

>> 
```
This is functionally identical to the menu prompt you see when you first run the program.

NOTE: This program will run until the user tells it to quit.

### Slope
The program will prompt you with the following output:
```
How many numbers are in the series:
>> [VALUE]

Please enter the first term of the series:
>>[VALUE]
Please enter the following term of the series:
>>[VALUE]
...
Please enter the last term of the series:
>>[VALUE]
```
After the user has finished entering the inputs, the program will return the sum of the terms of the series.

### Fibonacci Sequence
The program will prompt you with the following output:
```
Please enter to which term you would like to calculate the Fibonacci Sequence:
>> 
```
The program will calculate the value of the Fibonacci Sequence to the nth term specified by the user.

### Change Calculator
The program will prompt you with the following output:
```
Please input a dollar amount:
>> 
```
The program will use a greedy algorithm to determine the smallest number of bills and coins needed to represent that amount.  The program will present the following output:
```
Hundreds: [VALUE]
Fifties: [VALUE]
Twenties: [VALUE]
Tens: [VALUE]
Fives: [VALUE]
Ones: [VALUE]
Quarters: [VALUE]
Dimes: [VALUE]
Nickels: [VALUE]
Pennies: [VALUE]
```
