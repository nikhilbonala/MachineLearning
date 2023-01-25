'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#question6

string = "I am a teacher and I love to inspire and teach people"
string=string.split()       #split() Split  string into a list where each word is a list item as space as separator 
#to remove repeated elements we can convert list to set so that repeated elements will be removed
string=set(string)
print("Number of unique words present are =",len(string))   #as set contains only unique elements len() returns count of unique words
