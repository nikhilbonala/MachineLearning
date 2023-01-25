
#question 2
#2.1 Create an empty dictionary called dog
dog={}

#2.2 Add name, color, breed, legs, age to the dog dictionary
#added values and keys accordingly
dog["name"]="Julie"
dog["breed"]="pug"
dog["color"]="black"
dog["legs"]=4
dog["age"]=1

#2.3 Create a student dictionary and add first_name, last_name, gender, age, marital status,
#skills, country, city and address as keys for the dictionary
student={"first_name":"Rahul",
        "last_name":"M",
        "gender":"Male",
        "age":21,
        "marital_status":"Single",
        "Skills":["Java","SQL"],
        "Country":"USA",
        "Address":"Overland park"}

#2.4 Get the length of the student dictionary
length_student=len(student)                                 #used len() predefined function to get student Length
print("Length of dictionary=",length_student)

#2.5 Get the value of skills and check the data type, it should be a list

print("skills are=",student["Skills"])                      #accessing student skills using skills key
print("skills data type is=",type(student["Skills"]))       #used type() to find data type 

#2.6 Modify the skills values by adding one or two skills

student["Skills"].extend(["python","c"])                    #added extra skill by extend() method as student["Skills"] is list
print("Skills after adding=",student["Skills"])

#2.7 Get the dictionary keys as a list

print("Keys present in student dict=",student.keys())           #to get keys in dictionary used keys() predined method

#2.8 Get the dictionary values as a list

print("values present in student dict=",student.values())       #to get values in dictionary used values() predfined method
