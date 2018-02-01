'''
Rules:
Variable Length (Default Min is 8)
Upper and Lower Case
Numbers
Char 6-15 = Weak
Char 16+ = Strong
Default Symbols: ` ! " ? $ ? % ^ & * ( ) _ - + = { [ } ] : ; @ ' ~ # | \ < , > . ?
'''

import random
import hashlib

def pw_generator(rules, pw_length):
	strong_pw = ""
	for i in range(pw_length):
		diverse = False
		#print("Current PW Build", strong_pw)
		while not diverse:
			char_type = random.choice(rules)
			i = random.choice(char_type)
			if len(strong_pw) >= 3 and strong_pw[-1] == i and strong_pw[-2] == i:
				print("Repetition detected. Rechoosing random character.")
				diverse = False
			else:
				diverse = True
		strong_pw += i
	return strong_pw

def yes_no(rule_string):
	error = "\033[0;31m"+"Invalid Input. Try Again with (Y/N)"+ "\033[0m"
	while 1:
		user_decision = input("Allow %s (Y/N): " % rule_string)
		if len(user_decision) == 0:
			print(error)
			continue
		if user_decision[0].lower() == "y":
			rule = True
			break
		elif user_decision[0].lower() == "n":
			rule = False
			break
		else:
			print(error)
	return rule

def print_pw(s):
	print("**********************************************************************")
	print("Plaintext Password:", s)
	print("MD5:\t",    hashlib.md5(s.encode()).hexdigest())
	print("SHA1:\t",   hashlib.sha1(s.encode()).hexdigest())
	print("SHA224:\t", hashlib.sha224(s.encode()).hexdigest())
	print("SHA256:\t", hashlib.sha256(s.encode()).hexdigest())
	print("SHA384:\t", hashlib.sha384(s.encode()).hexdigest())
	print("SHA512:\t", hashlib.sha512(s.encode()).hexdigest())
	print("**********************************************************************")

if __name__ == "__main__":

	pw_length = 16
	allow_upper = False
	allow_lower = False
	allow_num = False
	allow_symbols = False
	allow_default_symbols = True

	default_lower   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	default_upper   = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	default_num     = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	default_symbols = ["`",  "!", "\"", "?", "$",  "%", "^", "&", "*", "(", ")", 
					   "_",  "-", "+",  "=", "{",  "[", "}", "]", ":", ";", "@", 
					   "\'", "~", "#",  "|", "<", ",", ">", "."]
	user_symbols    = ""
	rules = []

	# Default Generated Password
	print("======================================================================")
	default_rules = [default_lower, default_upper, default_num, default_symbols]
	print("This is a randomly generated 16 character password.")
	print("There are (26+26+10+30)^16 possible combinations.")
	print("That is about 2.634e31 possible combinations.")
	print("NOTE: There is a little bit less than that since the program does not allow 3 characters to repeat consecutively.")
	print_pw(pw_generator(default_rules, pw_length))
	print("======================================================================\n")

	#exit()

	custom_pw = False
	custom_pw = yes_no("Custom Password")
	if custom_pw == False:
		exit()

	p1 = False
	while not p1:
		def isanumber(p):
			try:
				int(p)
				return True
			except ValueError:
				try:
					float(p)
					return False
				except ValueError:
					return False

		pw_length = input("Max length of PW? (Must be greater than 8): ")
		p1 = isanumber(pw_length)
		if p1 and int(pw_length) < 8:
			print("\033[0;31m"+"Invalid Input. Try Again with an Length 8 or Greater."+ "\033[0m")
			p1 = False
			continue
		if p1 == False:
			print("\033[0;31m"+"Invalid Input. Try Again with an Integer."+ "\033[0m")

	# Successful
	pw_length = int(pw_length)

	# Allow Rules? If so, append to rules list
	allow_upper   = yes_no("Upper Case")
	if allow_upper:
		rules.append(default_upper)

	allow_lower   = yes_no("Lower Case")
	if allow_lower:
		rules.append(default_lower)

	allow_num     = yes_no("Numbers")
	if allow_num:
		rules.append(default_num)

	allow_symbols = yes_no("Symbols")
	if allow_symbols:
		print("Default Symbols: ` ! \" $ ? % ^ & * ( ) _ - + = { [ } ] : ; @ \' ~ # | < , > .")
		allow_default_symbols = yes_no("Default Symbols")
		if allow_default_symbols:
			rules.append(default_symbols)

	# Custom Symbols
	if not allow_default_symbols:

		while len(user_symbols) == 0:
			user_symbols = list(input("Enter Custom Symbols, Not Characters/Numbers! (with no spaces or dividers):"))
			
			# Empty input
			if len(user_symbols) == 0:
				print("You must enter a value.")
				continue

			# Remove duplicates
			user_symbols = list("".join(set(user_symbols)))

			# Remove alphas and nums
			filtered_input = []
			for symbol in user_symbols:
				if not symbol.isalnum():
					filtered_input += symbol
			user_symbols = filtered_input

			# In case all characters were pre-existing
			if len(user_symbols) == 0:
				print("Entered only pre-existing characters. Add different characters!")
		
		print("Your custom characters:", str(user_symbols))
		rules.append(user_symbols)

	if not allow_lower and not allow_upper and not allow_num and not allow_symbols:
		print("You literally have an empty string as a password.")
		print("Bad user! Try again and do better!")
		exit()
		
	print_pw(pw_generator(rules, pw_length))
