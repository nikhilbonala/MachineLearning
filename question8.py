'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
'''
Question 8
Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
“The area of a circle with radius 10 is 314 meters square.”
'''
#using .format() for string formatting and used placeholders in curly braces to format string
print("radius = {radius}".format(radius=10))            
print("area = {pi} * {radius} ** 2".format(pi=3.14,radius=10))

radius = 10
area = 3.14 * radius ** 2
#  used precision of the floating-point values for area :.0f
print("The area of a circle with {radius} is {area:.0f} meters square.".format(radius=radius,area=area))
