#Program: Jikan - Japanese Calendar Test Program
#Version: Terminal Version
#Programmer: Joseph Ferrer
#Email:joferrer16@gmail.com
#Github Username: joeferrer


from random import randrange
from operator import add
from modules.user_end import get_input
from modules.user_end import get_game_mode
from modules.japs_lib import get_dict_jap_month
from modules.japs_lib import get_list_jap_days
from modules.japs_lib import get_list_jap_nums
import modules.app_struct

def str_dayn(x):
	r = x%10
	string = ""
	if r == 1:
		string = str(x) + "st"
	elif r == 2:
		string = str(x) + "nd"
	elif r==3:
		string = str(x) + "rd"
	else:
		string = str(x) + "th"
	return string
	

if __name__ == "__main__":
	M = get_dict_jap_month()
	D = get_list_jap_days('')
	Y = get_list_jap_nums('')
	
	modules.app_struct.I_INTRO("Karendaa Terminal Version","Joe Ferrer","joferrer16@gmail.com","github.com/joeferrer")
	modules.app_struct.I_GMODE("1")
	game_mode = get_game_mode()

	if game_mode.lower() == "a":
		modules.app_struct.I_INSTR("2","\nA random date will be generated\nYou're objective is to translate it to Japanese!")
		modules.app_struct.I_EX("Generated Date. = '6th of November 2010'\nAnswer = 'nisenjuunen juuichigatsu muika'.")
		modules.app_struct.I_NOTE("","\n","Note: Remember to put the needed spaces.")
	else:
		modules.app_struct.I_INSTR("2","\nA random date in Japanese will be generated\nYou're objective is to give its corresponding date.")
		modules.app_struct.I_EX("Generated JapDate. = 'nisenjuunen juuichigatsu muika'\nAnswer = '6th of November 2010'\nNote: Remember to put the needed spaces.")

	modules.app_struct.I_CASE("3")
	modules.app_struct.I_QR("4")
	modules.app_struct.I_START("5")
	get_input()

	print "Ganbatte Kudasai! START!\n\n"

	while 1==1:
		day = randrange(1,32,1)
		month = randrange(1,13,1)
		year = randrange(1700,2301,1)	
		
		eq = str_dayn(day) + " of " + M.keys()[month%12] + " " + str(year) 
		if day != 20:
			jday = D[0][day] if day < 11 else [D[2][day/10] + D[1][day%10]] 
			if day >=11 and ((day - (day/10)*10) != 4):
				jday = map(add,jday,['nichi']*len(jday))
		else:
			jday = ['hatsuka']
		jmonth = M[M.keys()[month%12]]
		jyear = Y[3][year/1000] + Y[2][(year%1000)/100] + Y[1][(year%1000)%100/10] + Y[0][((year%1000)%100)%10/1] +"nen"
		jq = []
		for i in jday:
			jq.append(jyear + " " + jmonth + " " + i)

		if game_mode.lower() == 'a':
			print eq.lower()
			print "Nannichi desu ka"
			user_answer = get_input()
			if user_answer.lower() == "quit":
				break
			elif user_answer.lower() == "reset":
				print "\nChoose the  game mode:\nA) Date->Japanese	B)Japanese->Date: "
				game_mode = get_game_mode()
				print "\n"
				continue
			elif user_answer.lower() in [x.lower() for x in jq]:
				print "Correct!\n\n"
			else:
				print "Incorrect!\nThe answer is " + str(jq).lower() + "\n\n"
			
		else:
			print [str(jq).lower()][0]
			print "What is the date?"
			user_answer = get_input()
			if user_answer.lower() == "quit":
				break
			elif user_answer.lower() == "reset":
				print "\nChoose the  game mode:\nA) Date->Japanese	B)Japanese->Date: "
				game_mode = get_game_mode()
				print "\n"
				continue
			elif user_answer.lower() == eq.lower():
				print "Correct!\n\n"
			else:
				print "Incorrect!\nThe answer is " + eq.lower() + "\n\n"

	print "\n\nDomo Arigatou Gozaimasu!"