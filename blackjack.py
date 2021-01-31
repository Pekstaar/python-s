#This is a black jack game.
	# create a list of 13 cards picking cards randomly:
	 # create 2 users: user and system.
	 # Start game with the user having 2 (random) cards and 1 card for the system
	 # calculate the total score of the 2 random cards: 
	  # if user a blackjack(Ace + 10 = 21) opponent loses and break(get to final step).
	  # if false continue playing.
	   # draw another card for the user, calculate the total score and display it
			# .if card picked is an ace and total score is above 21 have it as 21)
	   # prompt user whether to pick another card 
	    # if yes randomly pick another card, display it and have the score query for the total
	   # once user is done(picks no for game continuation) let the system play
	   #compare the 2 players score and the highest(not above 21) should be the winner
	   #finally print the users final result 
	   #Ask user whether to play another game and if true call the game function again else exit 	    
	    
import art
import random
	   				

print(art.blackjack) #game logo
#------- gaming function begins here -------
def game():
	#create cards
	Ace=11
	cards = [Ace,2,3,4,5,6,7,8,9,10]
	#create users
	ran = random.choice(cards)
	score = 0
	system = 0
	#start game
	# system random card
	system += random.choice(cards)
	#user random card total
	score += random.choice(cards) + random.choice(cards)
	#blackjack
	blackjack = False;			
	#-------- game play loop begins here -------		
	while(not blackjack):
		#check users initial score.
		#if score is user equal to 21 set blackjack as true and print blackjack 
		if(score == 21):
			blackjack=True			
			print("You win! Black-Jack!")
		#check if score is greater than 21 and if true draw out of loop
		#system does not need to play here
		elif(score >=  21):
			break	
		#else score is less than 21 - continue to processes below	
		#print ('looping');
		#display score before user plays
		print(f"Your Score is: {score}")
		print(f"System Score is: {system}")
		#play by making choice
		choice = input("Pick another card? 'y' for yes 'n' for no: ")
		#based on users choice generate card if yes
		if((choice) == 'y'):
			your_pick = random.choice(cards)			 
			score += your_pick
			#print picked score
			print(f"You card is {your_pick} score: {score}")
			#continue
			#continue looping 
		#let system play		
		else:
			#add new card to system.
			system += random.choice(cards)
			#check if system is above or equal to 21 and if true break out of play.
			if(system >= 21):
				break
			#if not, create choice list of whether to play or not
			def make_choice():
				return random.choice([True,False])
				
			choice = make_choice()
			# coninue playing while boolean below is true
			print(f"While not in loop choice: {choice}")
			if(system <=14):
				choice = True
				
			while(choice):
				#add new card to system results
				system += random.choice(cards)
				#check if system results are below 21 and if true let system make choice whether to
				# continue.
				if(system < 21):
					#make choice
					ch = make_choice()
					print(f"while in loop System Choice: {choice}")
					print(f"System Results: {system}")
					#if choice is false break out of loop
					if(ch == False):
						break
					continue
				#if system scores is equal or above 21 stop play
				
				#choice == False
				continue
			break
			# -------- system play loop ends here --------		
					
	# --------- game play loop ends here ---------
		
	#display blackjack if true
	if(blackjack == True):
		print(f"your score: {score} system : {system}")
	#display results here if all is done
	print(f"System scores: {system}")
	print(f"You Score: {score}")

#------- gaming function ends here ------

game()











