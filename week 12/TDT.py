import json

# JSON string:
# Multi-line string
data ="""{
	"Name": "Jennifer Smith", 
	"Contact Number": 7867567898, 
	"Email": "jen123@gmail.com", 
	"Hobbies":["Reading", "Sketching", "Horse Riding"] 
	}"""

# parse data:
res = json.loads(data) #here i persed the Json string as an object and then convert this json data into the python dictionary.

# the result is a Python dictionary:
print(res)
import json

data = {
	"name": "Satyam kumar",
	"place": "patna",
	"skills": [
		"Raspberry pi",
		"Machine Learning",
		"Web Development"
	],
	"email": "xyz@gmail.com",
	"projects": [
		"Python Data Mining",
		"Python Data Science"
	]
}
with open( "data_file.json" , "w" ) as write:
	json.dump( data , write )
with open("data_file.json","r") as read:
    print(json.load(read)) #JSON FIle is parse as an object,thus json file is converted into python dictionary.