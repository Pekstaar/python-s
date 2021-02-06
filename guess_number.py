#
import art
import random

#print(art.guessNumber)
#print("Random Number: ",random.randrange(1,100,1))
#Guess Number game:
	# Display game name, logo 
	# Generate random Number
	# Input gaming stage "easy" or "hard"
	 # if easy, have 10 trials
	 # if hard, have 5 trials only
	#loop input number according to level selected.
	 # Rank gamers number selected: "above", "exact", "below"
	 # Continue playing if rank is above or below and display rank
	 # if exact end game(get of loop)
	 # if trials end, end game also
	 
#guess number function
print(art.guessNumber)
def guess(gNum,rNum):
	
	if gNum>rNum:
		return "Guess Too High!"
	elif gNum<rNum:
		return "Guess Too Low!"
	else: 
		return ""
		

#initialize number
random_number=random.randint(1,100)
trials = 0 #number of trials according to level
#input gaming stage
level=input("Input level 'hard' or 'easy': ")

if level=="hard":
	trials=5
elif level=="easy":
	trials=10

done=False
for _ in range(trials):
	#input guess
	gNum=int(input("Input number guessed: "))
	#rank guess
	print(guess(gNum,random_number))
	if random_number==gNum:
		print(f"Correct guess! in {_+1} trials")
		done=True
		break
	print(f"\n{trials-(_+1)} Guess(es) to go") 
if not done:
	print(f"\nThe Number was: {random_number}")

	
