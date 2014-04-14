
import sys

def get_input():
	version = sys.version_info
	if version[0] > 2:
		return input()
	else:
		return raw_input()

def get_game_mode():
	choice = "z"
	while choice.lower() != "a" and choice.lower() != "b":
		choice = get_input()
		if choice.lower() != "a" and choice.lower() != "b":
			print "Invalid input. Choose between 'A' and 'B' only!"
	return choice