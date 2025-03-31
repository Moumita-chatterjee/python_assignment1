'''Created on: 17-01-2025
Created by: Moumita
Objective :8. Write a program to convert Fahrenheit into Celsius. Take Fahrenheit as input.
'''

fahrenheit = int(input("Enter the temp in Fahrenheit: "));
#Formula for converting Fahrenheit to celsius
celsius = (fahrenheit - 32) * 5/9;
#Print the value with one decimal point
print ("Show the value of temp in celsius: ", round(celsius,1));