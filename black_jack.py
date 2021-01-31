#commment
import random
import os
import art

#create deal cards function
def deal_card():
	"""Returns a random card from cards deck"""
	cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
	card = random.choice(cards)
	
	return card
#calculate score function
def calculate_score(cards): 
	"""Takes a list of cards and calculate the total value"""
	if sum(cards)==21 and len(cards)==2:
		return 0
	if 11 in cards and sum(cards)>21:
		cards.remove(11)
		cards.append(1)		
	#sum up iterables
	return sum(cards)
#compare the two players scores funcion
def compare(score_1, score_2):
	if score_1 == score_2:
		#this is a draw
		return("  Draw!")
	elif score_2 == 0:
		return "  Lose! Opponent has a blackjack!"
	elif score_1 == 0:
		return "  You win with a blackjack!"
	elif score_1 > 21:
		return "  Score over limit! You lose."	
	elif score_2 > 21:
		return "  Opponent is over limit! You Win!!"
	elif score_1 > score_2:
		return "  You win!"
	else:
		return "  You Lose!"
		
#deal user and computer 
#gaming function
def play_game():
	#Logo call
	print(art.blackjack)
	
	user_cards=[]
	computer_cards=[]
	is_game_over = False

	for _ in range(2):
		user_cards.append(deal_card())
		computer_cards.append(deal_card())

	#user calculation while loop
	while not is_game_over:
		user_score = calculate_score(user_cards)
		computer_score = calculate_score(computer_cards)

		print(f"  Your Cards: {user_cards}, current score: {user_score}")
		print(f"  Computer card: {computer_cards[0]}")

		if user_score == 0 or computer_score == 0 or user_score > 21:
			is_game_over = True	
		else: 
			continue_play = input("  Type 'y' to continue playing and 'n' to end game: ")
			if(continue_play == "y"):
				user_cards.append(deal_card())
			else: is_game_over = True
			
	#computer calculation while loop 
	while computer_score != 0 and computer_score < 17:
		computer_cards.append(deal_card())
		computer_score = calculate_score(computer_cards)

	#calculate result!
	#display final results
	print(f"  Your final cards: {user_cards}, Your score: {user_score}")
	print(f"  Computer final cards: {computer_cards}, Computer Score: {computer_score}") 
	print(compare(user_score, computer_score))

	#ask user if should restart game
while input("Play Blackjack game? Type 'y' or 'n': ") == 'y':
	os.system('clear')
	play_game()	
	
	
	
	
	
	
	

	
