'''Created on: 17-01-2025
Created by: Moumita
Objective : 6. Take the marks of a student obtained in 5 subjects (each out of 100), write a program
to calculate total marks and percentage marks.
'''
science = int(input("Enter a marks for science:" ));
maths = int(input("Enter a marks for maths:" ));
english = int(input("Enter a marks for english:" ));
hindi = int(input("Enter a marks for hindi:" ));
sst = int(input("Enter a marks for sst:" ));

total = science + maths + english + hindi + sst;
percentage = (total /500) * 100;
print("Total marks obtained:",total,"Overall percentage of a student:",percentage);