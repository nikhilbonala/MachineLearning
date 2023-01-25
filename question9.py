
N=int(input("Enter number students:")) #N is number of students
student_weight_lb=[] #list to store student weight in pounds
student_weight_kg=[] #list to store student weight in kilograms
while(N):  #used while loop to take list of weights from console
    weight=int(input()) 
    student_weight_lb.append(weight) 
    N=N-1
for weight in student_weight_lb: #iterated through student_weight_lb list by using 'for' loop
    kg=round(weight*0.454,2)    #conversion of pounds to kg and rounding decimal values
    student_weight_kg.append(kg)    # adding converted value to student_weight_kg list
print(student_weight_kg)
