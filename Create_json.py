import json

# create a dictionary object
person_dict = {'first': 'Christopher', 'last': 'Harrison'}

# Add dictionary key pairs to dictionary as needed
person_dict['city']='Seattle'

#convert dictionary to json object
person_json = json.dumps(person_dict)


#print JSON object
print(person_json)

###### Create JSON with nested dictionary#########

#Create a staff dictionary 
#assign a person to a staff posiyion of program manager
staff_dict={}
staff_dict['Program Manager']= person_dict

staff_json = json.dumps(staff_dict)

print(staff_json)