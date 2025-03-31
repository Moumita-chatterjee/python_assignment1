'''Created on: 10-01-2025
Created by: Moumita
Objective : Python Assignment1
'''
#1. Length and breadth of a rectangle are taken as user input.
#Write a program to calculate the area and perimeter of the rectangle.

#Take the inputs from the user
a_len = int(input("Enter the length of a rectangle:" ));
b_bre = int(input("Enter the breadth of a rectangle:" ));

#calculate the area and perimeter of a rectangle
area = a_len * b_bre;
peri = 2*(a_len + b_bre);
print("Area of a rectangle =", area);
print("Perimeter of a rectangle = ", peri);