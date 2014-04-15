#Program: Tango - General Japanese Vocabulary Tester Program
#Version: Terminal Version
#Programmer: Joseph Ferrer
#Email:joferrer16@gmail.com
#Github Username: joeferrer



import random
from modules.user_end import get_input
from modules.user_end import get_game_mode
from modules.user_end import get_word_type
import modules.app_struct

if __name__ == "__main__":

	modules.app_struct.I_INTRO("Tango Terminal Version","Joe Ferrer","joferrer16@gmail.com","github.com/joeferrer")
	modules.app_struct.I_GMODE("1")
	game_mode = get_game_mode()

	if game_mode.lower() == "a":
		modules.app_struct.I_INSTR("2","\nA random English word/phrase will be displayed.\nYou must first identify if the word is in Hiragana 'H' or Katakana 'F' or\n'FH' if in Katakana-Hiragana form or 'HF' if in Hiragana-Katakana form.\nThen, translate the word to Japanese.")
	else:
		modules.app_struct.I_INSTR("2","\nA random Japanese word/phrase will be displayed.\nYou must first identify if the word is in Hiragana 'H' or Katakana 'F' or\n'FH' if in Katakana-Hiragana form or 'HF' if in Hiragana-Katakana form.\nThen, translate the word to English.")

	modules.app_struct.I_NOTE("3.) ","\n\n","Note, if you use 'ee' for prolonged 'e' stick to doubling like that for all other cases such as 'oo' vice-versa.\nOtherwise, if you use 'ei' stick to doubling like that and for other cases like 'ou',vice-versa.\nExample: if 'oo' kookoosee NOT kookoosei.\n\nAlso note that 'masu' forms of verbs will not be accepted as the objective here is to know the dictionary form only.")
	
	modules.app_struct.I_CASE("4")
	modules.app_struct.I_QR("5")
	modules.app_struct.I_START("6")
	get_input()

	print "Ganbatte Kudasai! START!\n\n"


	F = open("_ext-files/vocabulary.txt")
	D = dict()
	while True:
		line = F.readline()
		if line == '':
			break
		line = line.strip('\n')
		parsed = line.split(";")
		e_str = parsed[0]
		j_str = parsed[1:len(parsed)]
		
		D.update({e_str:j_str})
	K = D.keys()	
	#print D	
	
	user_answer_wt=""
	user_answer_wd=""
	looper = 1
	R = 1 #Round Counter
	while looper==1:
		random.shuffle(K)
		mistakes = 0
		count = 1 #Item Counter
		print "\nRound " + str(R) + "\n\n"
		for i in K:
			print str(count) + " out of " + str(len(K)) + "; mistakes=" + str(mistakes) 
			count = count + 1
			if game_mode.lower() == "a":
				temp = D[i]
				print i.split("/")
				print "Japanese Translation: "
				user_answer_wd = get_input()
				if user_answer_wd.lower() == "quit":
					looper = 2
					break
				elif user_answer_wd.lower() == "reset":
					print "\nChoose the  game mode:\nA) English->Japanese	B)Japanese->English: "
					game_mode = get_game_mode()
					R = 0
					break	
				print "Word Type(H/F/FH/HF only): "
				user_answer_wt = get_word_type()
				if (user_answer_wt.lower() == temp[len(temp)-1].lower()) and (user_answer_wd.lower() in [x.lower() for x in temp[0:len(temp)-1]]):
					print "Correct!\n\n"
				else:
					print "Incorrect!"
					print "Word-Type = " + str(temp[len(temp)-1])
					print "Japanese = " + str(temp[0:len(temp)-1]) + "\n\n"
					mistakes = mistakes + 1
			else:
				temp = D[i]
				e_temp = i.split("/")
				print temp[0:len(temp)-1]
				print "English Translation: "
				user_answer_wd = get_input()
				if user_answer_wd.lower() == "quit":
					looper = 2
					break
				elif user_answer_wd.lower() == "reset":
					print "\nChoose the  game mode:\nA) English->Japanese	B)Japanese->English: "
					game_mode = get_game_mode()
					R = 0
					break	
				print "Word Type(H/F/FH/HF only): "
				user_answer_wt = get_word_type()
				if (user_answer_wt.lower() == temp[len(temp)-1].lower()) and (user_answer_wd.lower() in [x.lower() for x in e_temp[0:len(e_temp)]]):
					print "Correct!\n\n"
				else:
					print "Incorrect!"
					print "Word-Type = " + str(temp[len(temp)-1])
					print "English = " + str(e_temp) + "\n\n"
					mistakes = mistakes + 1
		score = len(K) - mistakes
		if looper==1 and R != 0:
			print "Your score is " + str(score) + "/" + str(len(K)) + "\n\n"	
		R = R + 1											
	F.close()

	print "\n\nDomo Arigatou Gozaimasu!"				




	