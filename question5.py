'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#question5

from math import pi     # imported pi variable from math library
radius=30
#5.1 Calculate the area of a circle and assign the value to a variable name of _area_of_circle_

_area_of_circle_ = pi * radius * radius         #as area of circle is π × radius2
print("Area of circle = ",round(_area_of_circle_,2))

#5.2 Calculate the circumference of a circle and assign the value to a variable name of _circum_of_circle_
_circum_of_circle_ = 2 * pi * radius        #as circumference of circle is 2 x π × radius
print("circumference of circle = ",round(_circum_of_circle_,2))

#5.3 Take radius as user input and calculate the area.
radius=int(input("Enter radius of circle ="))       #took radius as input from user
_area_of_circle_ = pi * radius * radius             #as area of circle is π × radius2
print("Area of circle = ",round(_area_of_circle_,2))
