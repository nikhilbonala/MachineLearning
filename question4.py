'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#question4

#4.1 Find the length of the set it_companies
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print("length of it_companies=",len(it_companies))      #used len() to find length of it_companies set

#4.2 Add 'Twitter' to it_companies

it_companies.add("Twitter")                             #used add() predefined function to add twitter to it_companies 
print("added twitter to set",it_companies)

#4.3 Insert multiple IT companies at once to the set it_companies

it_companies.update({"FEDEX","SAMSUNG"})            #to insert multiple values into set used update()
print("it_companies after adding multiple elements=",it_companies)

#4.4 Remove one of the companies from the set it_companies

it_companies.remove("Google")                   #remove() to remove item from set
print("it_companies after removing Google=",it_companies)

#4.5  What is the difference between remove and discard
'''Remove method throws Keyerror if the element is not present in the SET where as discard doesnt throw any error'''

#4.6 Join A and B
unionSet=A.union(B)                     #union() will return set contains all elements of A and B 
print("Join of A and B=", unionSet)

#4.7 Find A intersection B
print("intersection of A and B=",A.intersection(B))     #intersection() returns a set of common values present in sets A and B

#4.8 Is A subset of B
print("Is A subset of B =",A.issubset(B))           #issubset() returns a boolean value of condition A subset of B or not

#4.9 Are A and B disjoint sets
print("Are A and B disjoint sets =",A.isdisjoint(B))        #isdisjoint() returns a boolean value of condition A and B are disjoint sets

#4.10 Join A with B and B with A
temp_A=A.copy()                         #stored A set in temporary set to keep its original values which can be used to join with B
A.update(B)                             #To join A with B 
B.update(temp_A)                        #To join B with A
print("Join A with B =",A)
print("Join B with B =",B)

#4.11 What is the symmetric difference between A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
#symmetric_difference() returns set which contains the elements which are either in set A or in set B but not in both 
print("symmetric difference between A and B=",A.symmetric_difference(B))

#4.12 Delete the sets completely

del A           #del permanently delete set
del B

#4.13 Convert the ages to a set and compare the length of the list and the set.

ages_set=set(age)                   #converting age list to set and storing in ages_set
print("age set =",ages_set)             
print("length of ages set is =",len(ages_set))      #set removes repeated elements so length decreases 
print("length of ages list is =",len(age))
