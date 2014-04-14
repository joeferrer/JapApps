#Program: Jikan - Japanese Time Tester Program
#Version: Terminal Version
#Programmer: Joseph Ferrer
#Email:joferrer16@gmail.com
#Github Username: joeferrer

from random import randrange
from modules.user_end import get_input
from modules.user_end import get_game_mode

def str_minutes(x):
	if x < 10:
		minutes = "0"+str(x)
	else:
		minutes = str(x)
	return minutes

if __name__ == "__main__":

	print "\nWelcome To 'Jikan Terminal Version'\nCreated by Joe Ferrer\nEmail:joferrer16@gmail.com\nGithub:joeferrer\n\n"
	print "INSTRUCTIONS\n"

	print "1.) Choose the  game mode:\nA) Time->Japanese	B)Japanese->Time: "
	game_mode = get_game_mode()

	if game_mode.lower() == "a":
		print "\n\n2.) Okay! Here's what you're supposed to do.\nA random time will be generated\nYou're objective is to translate it to Japanese!"	
		print "\n\nExample: Generated No. = 3:45 AM\nAnswer = 'gozen sanjiyonjuugofun'\nNote: Put a space after gozen/gogo."
	else:
		print "\n\n2.) Okay! Here's what you're supposed to do.\nA random time in Japanese will be generated\nYou're objective is to give its corresponding time."
		print "\n\nExample: Generated JapNo. = 'gozen sanjiyonjuugofun'\nAnswer = 3:45 AM\nNote: Put a space before AM/PM."

	print "\n\n3.) Note: For simplicity's sake, 'han' and other like terms will not be accepted.\ni.e. 30 min = sanjuupun\n\nAlso for simplicity, 8 min = happun NOT hachifun."
	print "\n\n4.) Answers are NOT case sensitive"
	print "\n\n5.) You can quit at any point in the game by typing 'quit'.\nYou can reset the game by typing 'reset'."
	print "\n\n6.) Press enter key to start..."
	get_input()

	print "Ganbatte Kudasai! START!\n\n"

	D = []
	D.append(['pun','ippun','nifun','sanpun','yonpun','gofun','roppun','nanafun','happun','kyuufun','juppun'])
	D.append(['','juu','nijuu','sanjuu','yonjuu','gojuu'])
	D.append(['','ichiji','niji','sanji','yoji','goji','rokuji','shichiji','hachiji','kuji','juuji','juuichiji','juuniji'])
	D.append(['','gozen','gogo',"AM","PM"])
	
	user_answer = ""
	while 1==1:
		H = randrange(1,13,1)
		M = randrange(1,60,1)
		R = randrange(1,3,1)
		ans_j = str(D[3][R]) + " " +  str(D[2][H]) + str(D[1][M/10] + str(D[0][M%10])) 
		ans_e = str(H) + ":" + str_minutes(M) + " " + str(D[3][R+2]) 

		if game_mode.lower() == "a":
			print ans_e
			print "Ima nanji desu ka"
			user_answer = get_input()
			if user_answer.lower() == "quit":
				break
			elif user_answer.lower() == "reset":
				print "\nChoose the  game mode:\nA) Time->Japanese	B)Japanese->Time: "
				game_mode = get_game_mode()
				print "\n"
				continue
			elif user_answer.lower() == ans_j.lower():
				print "Correct!\n\n"
			else:
				print "Incorrect!\nThe answer is " + ans_j + "\n\n"
		else:
			print ans_j
			print "What time is it now? "
			user_answer = get_input()
			if user_answer.lower() == "quit":
				break
			elif user_answer.lower() == "reset":
				print "\nChoose the  game mode:\nA) Time->Japanese	B)Japanese->Time: "
				game_mode = get_game_mode()
				print "\n"
				continue
			elif user_answer.lower() == ans_e.lower():
				print "Correct!\n\n"
			else:
				print "Incorrect!\nThe answer is " + ans_e + "\n\n"

	print "\n\nDomo Arigatou Gozaimasu!"	