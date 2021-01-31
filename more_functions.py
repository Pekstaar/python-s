#--------- More on functions -------------
#functions with outputs
#Title casing function

import art 

def format_name(f_name, l_name):
	#check if parameters are empty.
	if(f_name=="" or l_name==""):
		#Early return
		return "Inputs empty!"
	
	formated_f_name = f_name.title()
	formated_l_name = l_name.title()
	
	#statement below returns string output
	#this is the functions output
	return f"{formated_f_name} {formated_l_name}"
	
#formatted = format_name(input("Input first Name: "), input("Input Last name: "))
#print(formatted)


#quiz:
	#leap year function(year parameter):
	 #check if divided by 4 remainder is zero and not divisible by 100 is_leap_year
	  #check if divided by 400 remainder is 0 is leap year
	  
       # days in month function (month parameter) - if :-
        # check days of the month(index) in months list
        # create list of days:
        
#leap year function        
def is_leap(year):
	if((year % 4) == 0 and (year % 100) != 0):
		return True;
		
	elif((year % 400) == 0):
		return True;
		
	else: return False;
	
#print(is_leap(int(input("Input year: "))))

#Days of the month function
def days_of_month(month_index, year=2000):
	
	#multiline comment or Doc String
	'''Input month index as first parameter and year as second whose default value is 2000'''
	feb = 28
	month = int(month_index)
	
	if (is_leap(int(year))):
		feb = 29
		
	months = [31,feb,31,30,31,30,31,31,30,31,30,31]
	
	if(month > 12 or month == 0): 
		return("Invalid Month")
	else:
		no_of_days = month - 1	
	
	return months[no_of_days]
	
#print(days_of_month(input("Input month to check: "), input("Input Year: "))) 		

#Doc Strings - documentations as one codes.
	#     - use """ String \n String \n """

#Calculator Project.

#Add function
def add(n1, n2):
	return n1 + n2
#Subtraction	
def subtract(n1, n2):
	return n1-n2	

#muliplication
def multiply(n1, n2):
	return n1*n2

#Division
def divide(n1, n2):
	return n1/n2

#signs dictionary		
signs_dictionary = {
	"+":add,
	"-":subtract, 
	"*":multiply, 
	"/":divide
 }

def calculator():

	print(art.calculator)

	num1 = float(input("Input First number: "))

	print("\nInput: ")
	for sign in signs_dictionary:
		print("'",sign,"'")
		
	use_answer = True;

	while use_answer:
		operand = input("Pick an operation symbol above: ")
		num = float(input("input Second number: "))
		func = signs_dictionary[operand]
		result = func(num1,num)

		print(f"\n{num1} {operand} {num} = {result}")	


		cont = input(f"Type 'y' to continue calculating with {result} and 'n' to exit Calculation and 'off' to power off the Calculator: ")
		if(cont == "y"):
			num1=result
		elif(cont == 'off'):
			print("\n Good Bye!")
			break;
			
		#Below is Recursion(function call within itself)
		else: calculator()
				
calculator()		
		
       		
	
