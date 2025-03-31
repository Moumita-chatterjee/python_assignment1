'''Created on: 17-01-2025
Created by: Moumita
Objective :9. The total number of students in a class are 90 out of which 45 are boys. If 50% of the
total students secured grade 'A' out of which 20 are boys, then write a program to
calculate the total number of girls getting grade 'A'.
'''
#Total number of student in a Class
total_no_stu = 90;
#Number of boy's in a class
boys = 45;
#Total number of students got grade 'A' in the class
stu_got_a = (50/100) *90;
#Total number of boys got 'A' in the class
no_boys_got_a = 20;
#Total number of girls got 'A' in the class
no_girls_got_a = stu_got_a - no_boys_got_a;

print("Total number of girls got 'A' in the class: " ,no_girls_got_a);
