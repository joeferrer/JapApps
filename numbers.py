#Program: Bangoo Tango - Japanese Number Vocabulary Tester Program
#Version: Terminal Version
#Programmer: Joseph Ferrer
#Email:joferrer16@gmail.com
#Github Username: joeferrer

from random import randrange
from operator import add
import sys

def get_input():
	version = sys.version_info
	if version[0] > 2:
		return input()
	else:
		return raw_input()

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
			
def get_game_mode():
	choice = "z"
	while choice.lower() != "a" and choice.lower() != "b":
		choice = get_input()
		if choice.lower() != "a" and choice.lower() != "b":
			print "Invalid input. Choose between 'A' and 'B' only!"
	return choice

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

	D = []
	D.append([0,'ichi','ni','san','yon','go','roku','nana','hachi','kyuu'])
	D.append([0,'juu','nijuu','sanjuu','yonjuu','gojuu','rokujuu','nanajuu','hachijuu','kyuujuu'])
	D.append([0,'hyaku','nihyaku','sanbyaku','yonhyaku','gohyaku','roppyaku','nanahyaku','happyaku','kyuuhyaku'])
	D.append([0,'sen','nisen','sanzen','yonsen','gosen','rokusen','nanasen','hassen','kyuusen'])
	D.append(['man','ichiman','niman','sanman','yonman','goman','rokuman','nanaman','hachiman','kyuuman'])
	D.append([0,'juu','nijuu','sanjuu','yonjuu','gojuu','rokujuu','nanajuu','hachijuu','kyuujuu'])
	D.append([0,'hyaku','nihyaku','sanbyaku','yonhyaku','gohyaku','roppyaku','nanahyaku','happyaku','kyuuhyaku'])
	D.append([0,'sen','nisen','sanzen','yonsen','gosen','rokusen','nanasen','hassen','kyuusen'])
	D.append(['oku','ichioku','nioku','sanoku','yonoku','gooku','rokuoku','nanaoku','hachioku','kyuuoku'])
	D.append([0,'juu','nijuu','sanjuu','yonjuu','gojuu','rokujuu','nanajuu','hachijuu','kyuujuu'])
	D.append([0,'hyaku','nihyaku','sanbyaku','yonhyaku','gohyaku','roppyaku','nanahyaku','happyaku','kyuuhyaku'])
	D.append([0,'sen','nisen','sanzen','yonsen','gosen','rokusen','nanasen','hassen','kyuusen'])

	print "\nWelcome To 'Bangoo-Tango Terminal Version'\nCreated by Joe Ferrer\nEmail:joferrer16@gmail.com\n\n"
	print "INSTRUCTIONS\n"
	
	print "1.) Specify your maximum range for number generation.\nChoose r from 0-11 (i.e.10^r): "
	max_range = get_max_range()		

	print "2.) Choose the  game mode:\nA) Number->Japanese	B)Japanese->Number: "
	game_mode = get_game_mode()

	if game_mode.lower() == "a":
		print "\n\n3.) Okay! Here's what you're supposed to do.\nA random number will be generated from 1->10^r.\nYou're objective is to translate it to Japanese!"	
		print "\n\nExample: Generated No. = 1350\nAnswer = 'Sen-sanbyaku-gojuu' or 'Sensanbyakugojuu'\n\nNote: For 4,7,9 please use 'yon','nana','kyuu' respectively."
	else:
		print "\n\n3.) Okay! Here's what you're supposed to do.\nA random Japanese number will be generated from 1->10^r.\nYou're objective is to give its corresponding Arabic numerical equivalent!"
		print "\n\nExample: Generated JapNo. = 'Sen-sanbyaku-gojuu'\nAnswer = 1350\n\nNote: For 4,7,9 please use 'yon','nana','kyuu' respectively."

	print "\n\n4.) Answers are NOT case sensitive."
	print "\n\n5.) You can quit at any point in the game by typing 'quit'.\nYou can reset the maximum range by typing 'reset'."

	print "\n\n6.) Press enter key to start..."
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
				continue
			elif int(user_answer) == G:
				print "Correct!\n\n"
			else:
				print "Incorrect!\nThe answer is " + str(G) + "\n\n"
	
	print "\n\nDomo Arigatou Gozaimasu!"	
