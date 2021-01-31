#dictionary- composed of: key, value
#dictionary = {"dict1":"This is a dictionary", "dict2":"This is another dictionary."}
#Dictionary data retrieval - print(dictionary[dict1]) --prints - "this is ..." 
#Dictionary data addition - dictionary["loop"] = "this is a loop" --adds dictionary to 3 items.
#Dictionary wiping to empty - dictionary = {}
#Dictionary editing - dictionary["loop"] = {"This is an edited loop"} --additional words added.
#Dictionary looping: for item in dictionary:
#			print(item) --prints key items in dictionary.
#			print(dictionary[item] --prints value items.

##Grading system:

import art;
import os;

students_scores = {
	"Harry":81,
	"Ron":78,
	"Jasmine":99,
	"Draco":74,
	"Neville":62
}

student_grades = {} #empty dictionary

for student in students_scores:
	if(students_scores[student] < 70):
		#print(student," : Failed!")	
		student_grades[student] = "Failed"	
	elif((students_scores[student] < 80) and (students_scores[student] >= 70)):
		##print(student, " : Accepatable")
		student_grades[student] = "Accepatable"
	elif((students_scores[student] < 90) and (students_scores[student] >= 80)):
		#print(student, " : Exceeds Expectations!")
		student_grades[student] = "Expectations"
	elif((students_scores[student] <= 100) and (students_scores[student] >= 90)):
		#print(student, " : Outstanding!")
		student_grades[student] = "Outstanding!"
		
#print(student_grades)

#dictionaries nesting in another dictionary.
travel_log = {
	"france":{'cities_visited':["paris","lille","Dijon"]},
	"Africa":["Kenya","Uganda","Rwanda"]
}
#print(travel_log)

#Dictionary nesting in a list

travel_log = [{
	"country":"France",
	'cities_visited':["paris","lille",
	"Dijon"], "visits_attended":8
	},
	{
	"Continent":"Africa",
	'contries_visited':["Kenya","Uganda","Rwanda"],
	"visits_attended":3
	},
]

def new_lyn():
	print('\n')
#function to add to nested dictionary.
def dict_add(country_visited, cities_visited, times_visited):
	new_dict = {}
	new_dict["country"] = country_visited
	new_dict["cities_visited"] = cities_visited	
	new_dict["visits_attended"] = times_visited
	
	print("new Dictionary",new_dict)
	new_lyn()
	
	travel_log.append(new_dict)
	print("Appended List: ", travel_log)
	
country = "Canada"
cities = ["Toronto","Quaebec", "victoria","Edmonton"]
visits = 1

#dict_add(country, cities, visits)

#Quiz Test:
	 # Bid Program to create Dictionaries of people involved 
	 # should clear Screen when one Enters
	 # calculate the one with highest bid

#variables
highest={}

def bidder():
	finished = False;	
	bid_dictionary = {}
	
	x=1
	while not finished:
		print( art.axe)
		name = input("What's Your Name?: ")
		bid = input("What's Your Bid?: $")
		if(input("Are There Any other bidders? Type 'yes' or 'no': ") == "no"):
			finished = True;
		
		#bid_dictionary[key] = value
		
		bid_dictionary[name] = int(bid)
		if(int(bid) > x):
			x=int(bid)
			
			
		os.system('clear')
	
	for b in bid_dictionary:
		if(bid_dictionary[b] == x):
			highest[b] = bid_dictionary[b]
			print("The highest bidder is: ",b," : $",bid_dictionary[b])
			
	#print("x", x)

#calling the bidder function
bidder()














	

