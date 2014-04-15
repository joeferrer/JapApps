
def I_INTRO(prog_name,programmer,email,github):
	print "\nWelcome To '"+prog_name+"'\nCreated by "+programmer+"\nEmail:"+email+"\nGithub:"+github+"\n\n"
	print "INSTRUCTIONS\n"

def I_GMODE(inum):
	print inum + ".) Choose the  game mode:\nA) Date->Japanese	B)Japanese->Date: "

def I_INSTR(inum,string):
	print "\n\n" + inum + ".) Okay! Here's what you're supposed to do." + string

def I_NOTE(inum,spaces,string):
	print spaces + inum + string

def I_CASE(inum):
	print "\n\n" + inum + ".) Answers are NOT case sensitive."

def I_QR(inum):
	print "\n\n" + inum + ".) You can quit at any point in the game by typing 'quit'.\nYou can reset the game by typing 'reset'."

def I_START(inum):
	print "\n\n" + inum + ".) Press enter key to start..."

def I_EX(string):
	print "\n\nExample: " + string