'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#3.1 Create a tuple containing names of your sisters and your brothers 
brothers=("harry","john")
sisters=("sam","meghan")

#3.2 Join brothers and sisters tuples and assign it to siblings

siblings=brothers+sisters           #used  + operator to join brothers and siblings tuples
print("siblings=",siblings)

#3.3 How many siblings do you have?

print("Number of siblings=",len(siblings))      #used len() predefined function to find count 

#3.4 Modify the siblings tuple and add the name of your father and mother and assign it to family_members
#we cannot modify tuple as it is immutable
fatherName="SB"
motherName="VL"
family_members = siblings+(fatherName,motherName)  
#added fatherName and motherName to siblings tuple and created a new tuple family_members
print("family numbers=",family_members)
