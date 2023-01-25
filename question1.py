'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

#question1
ages=[19,22,19,24,20,25,26,24,25,24]
#1.1. Sort the list and find the min and max age
ages.sort()                 #used sort function to sort
min_element=ages[0]         #as list already sorted taking first element as minimum and last element as maximum
max_element=ages[-1]
print("The minimum element in the list is=",min_element) 
print("The minimum element in the list is=",max_element)
print("List after sorting", ages)

#1.2 Add the min age and the max age again to the list
ages.append(min_element)            #using append function to add min and max elements to list
ages.append(max_element)
print("list after appending minimum and maximum elements",ages)

#1.3  Find the median age (one middle item or two middle items divided by two)
ages.sort()                     #to find median we need to sort the list
length=len(ages)                
if(length%2==0):                #checking if length of list is even or odd
    median=(ages[length//2]+ages[(length//2)-1])/2          #if even take average two middle numbers as median
else:
    median=ages[length//2]                                  #else take middle number as median
print("median of list=",median)

#1.4 Find the average age (sum of all items divided by their number)
avg=sum(ages)/len(ages)                         #used sum() predefined function for sum of elements in the list 
print("Average of the list=",avg)               #getting count by using len() function

#1.5 Find the range of the ages (max minus min)
r=max_element-min_element               
print("Range of the list=",r)

