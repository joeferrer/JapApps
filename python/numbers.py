#Program: Bangoo Tango - Japanese Number Vocabulary Tester Program
#Version: Terminal Version
#Programmer: Joseph Ferrer
#Email:joferrer16@gmail.com
#Github Username: joeferrer

from random import randrange
from operator import add
from modules.user_end import get_input
from modules.user_end import get_game_mode
from modules.japs_lib import get_list_jap_nums
import modules.app_struct

def get_max_range():
	max_range = 1
	while max_range%10 != 0:
		try:
			max_range = 10**int(get_input())
			if max_range >= 10**12:
				max_range = 5 #just to keep it in the loop
				print "Invalid input. Choose r to be from 0-11 only!"
		except:
			print "Invalid input. Choose r to be from 0-11 only!"
	return max_range
			
def randomize(mode,max_range):
	if mode == 1:
		return randrange(1,max_range+1,1)
	else:
		ndigits = 1
		while ndigits==1:
			ndigits = randrange(1,len(str(max_range))+1,1)
		rnum = 0
		rmult = 1
		for i in range(1,ndigits):
			rnum = rnum + rmult*randrange(1,10,1)
			rmult = rmult*10
		return rnum	

if __name__ == "__main__":

	D = get_list_jap_nums(0)

	modules.app_struct.I_INTRO("Bangoo-Tango Terminal Version","Joe Ferrer","joferrer16@gmail.com","github.com/joeferrer")
	
	print "1.) Specify your maximum range for number generation.\nChoose r from 0-11 (i.e.10^r): "
	max_range = get_max_range()		

	modules.app_struct.I_GMODE("2")
	game_mode = get_game_mode()

	if game_mode.lower() == "a":
		modules.app_struct.I_INSTR("3","\nA random number will be generated from 1->10^r.\nYou're objective is to translate it to Japanese!")
		modules.app_struct.I_EX("Generated No. = 1350\nAnswer = 'Sen-sanbyaku-gojuu' or 'Sensanbyakugojuu'\n\nNote: For 4,7,9 please use 'yon','nana','kyuu' respectively.")
	else:
		modules.app_struct.I_INSTR("3","\nA random Japanese number will be generated from 1->10^r.\nYou're objective is to give its corresponding Arabic numerical equivalent!")
		modules.app_struct.I_EX("Generated JapNo. = 'Sen-sanbyaku-gojuu'\nAnswer = 1350\n\nNote: For 4,7,9 please use 'yon','nana','kyuu' respectively.")	

	modules.app_struct.I_CASE("4")
	modules.app_struct.I_QR("5")
	modules.app_struct.I_START("6")
	get_input()

	print "Ganbatte Kudasai! START!\n\n"

	user_answer = ""
	while 1==1:
		A = []
		G = randomize(randrange(1,3,1),max_range)
		g = G
		e = 0
		while G/10**e >= 10:
			e+=1
		i = 10**e
		while e != -1:
			if D[e][g/i] != 0:
				A.append(D[e][g/i])
			g %= i
			e -= 1
			i = 10**e

		ans_1 = reduce(add,A)
		ans_2 = reduce(add,map(add,A,['-']*(len(A)-1)+['']))
		
		if game_mode.lower() == "a":
			print G
			print "Type your answer: "
			user_answer = get_input()
			
			if user_answer.lower() == "quit":
				break
			elif user_answer.lower() == "reset":
				print "\n\nSpecify your maximum range for number generation.\nChoose r from 0-11 (i.e.10^r): "
				max_range = get_max_range()
				print "Choose the  game mode:\nA) Number->Japanese	B)Japanese->Number: "
				game_mode = get_game_mode()
				print "\n"
				continue
			elif user_answer.lower() == ans_1.lower() or user_answer.lower() == ans_2.lower():
				print "Correct!\n\n"
			else:
				if ans_1.lower() != ans_2.lower():
					print "Incorrect!\nThe answer is " + ans_1 + "\n...or " + ans_2 + "\n\n"
				else:
					print "Incorrect!\nThe answer is " + ans_1 + "\n\n"
		else:
			print ans_2
			print "Type your answer: "
			user_answer = get_input()
			
			if user_answer.lower() == "quit":
				break
			elif user_answer.lower() == "reset":
				print "\n\nSpecify your maximum range for number generation.\nChoose r from 0-11 (i.e.10^r): "
				max_range = get_max_range()
				print "Choose the  game mode:\nA) Number->Japanese	B)Japanese->Number: "
				game_mode = get_game_mode()
				print "\n"
				continue
			elif int(user_answer) == G:
				print "Correct!\n\n"
			else:
				print "Incorrect!\nThe answer is " + str(G) + "\n\n"
	
	print "\n\nDomo Arigatou Gozaimasu!"	
