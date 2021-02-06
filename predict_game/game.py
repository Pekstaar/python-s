#comment

import people_data
import random
import art
import os

#grab data to compare from external dictionary
loaded_data = people_data.data


print(art.highlow)
#function returning returning selected from list
def selected(index):
	return loaded_data[index]
	
#print(f"random number 1: {rand_num['opponent1']} number 2: {opponent2}")

#allow user input values of whom is greater
def inputs():
	return input("Who has More Followers? Type 'A' or 'b': ").lower()

#evaluate data of who is greater
def is_greater(val1,val2):
	if val1>val2:
		return val1
	else : return val2

def compare(n1,n2,choice):	
	count_1=n1['follower_count']
	count_2=n2['follower_count']
	
	greater_value = is_greater(count_1,count_2)
	
	if greater_value == count_1 and choice == 'a':
			return True
	elif greater_value == count_2 and choice == 'b':
			return True
	else: return False
	
#print(selected(opp1),'\n', selected(opp2))

#def comparison
#print(f"{opp1['name']}")  
#display result to user of whether true or false
#display data of the two opponents

#randomly generate 2 values of opponent id to choose


	
	
result = True
score=0
#print(is_greater(opp1['follower_count'], opp2['follower_count']))
while result ==  True:
	opp1 = selected(random.randint(1,len(loaded_data)-1)) #first random index
	opp2 = selected(random.randint(1,len(loaded_data)-1)) #second random index
	if opp1['name']==opp2['name'] : continue
	
	print(f"First: {opp1['name']}, {opp1['description']}, {opp1['country']}")
	#vs logo
	print(art.vs)

	#second opponent
	print(f"Second: {opp2['name']}, {opp2['description']}, {opp2['country']}")
	#print(f'{result}')
	#display opponents
	result = compare(opp1,opp2,inputs())
	
	if result == False:
		os.system('clear')
		print(art.highlow)
		print(f" Choice was wrong! ")
		print(f" Final Score: {score} point(s)")
		break
	else:
		print(result)
		score +=1
		print("\n")
		continue
	





