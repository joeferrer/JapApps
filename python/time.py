#Program: Jikan - Japanese Time Tester Program
#Version: Terminal Version
#Programmer: Joseph Ferrer
#Email:joferrer16@gmail.com
#Github Username: joeferrer

from random import randrange
from modules.user_end import get_input
from modules.user_end import get_game_mode
from modules.japs_lib import get_list_jap_mins
from modules.japs_lib import get_list_jap_hours
import modules.app_struct

def str_minutes(x):
	if x < 10:
		minutes = "0"+str(x)
	else:
		minutes = str(x)
	return minutes

if __name__ == "__main__":

	modules.app_struct.I_INTRO("Jikan Terminal Version","Joe Ferrer","joferrer16@gmail.com","github.com/joeferrer")
	modules.app_struct.I_GMODE("1")
	game_mode = get_game_mode()

	if game_mode.lower() == "a":
		modules.app_struct.I_INSTR("2","\nA random time will be generated\nYou're objective is to translate it to Japanese!")
		modules.app_struct.I_EX("Generated No. = 3:45 AM\nAnswer = 'gozen sanjiyonjuugofun'\nNote: Put a space after gozen/gogo.")
	else:
		modules.app_struct.I_INSTR("2","\nA random time in Japanese will be generated\nYou're objective is to give its corresponding time.")
		modules.app_struct.I_EX("Generated JapNo. = 'gozen sanjiyonjuugofun'\nAnswer = 3:45 AM\nNote: Put a space before AM/PM.")

	modules.app_struct.I_NOTE("3.) ","\n\n","Note: For simplicity's sake, 'han' and other like terms will not be accepted.\ni.e. 30 min = sanjuupun\n\nAlso for simplicity, 8 min = happun NOT hachifun.")	
	modules.app_struct.I_CASE("4")
	modules.app_struct.I_QR("5")
	modules.app_struct.I_START("6")
	get_input()

	print "Ganbatte Kudasai! START!\n\n"

	D = get_list_jap_mins('')
	D =  D + get_list_jap_hours('')
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