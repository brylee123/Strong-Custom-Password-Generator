'''
Rules:
Variable Length (Default Min is 8)
Upper and Lower Case
Numbers
Char 6-15 = Weak
Char 16+ = Strong
Default Symbols: ` ! " ? $ ? % ^ & * ( ) _ - + = { [ } ] : ; @ ' ~ # | \ < , > . ? /
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

def print_pw(s):
	print("Plaintext Password:", s)

	# MD5
	print("MD5:\t", hashlib.md5(s.encode()).hexdigest())

	#SHA1
	print("SHA1:\t", hashlib.sha1(s.encode()).hexdigest())

	#SHA224
	print("SHA224:\t", hashlib.sha224(s.encode()).hexdigest())
	
	#SHA256
	print("SHA256:\t", hashlib.sha256(s.encode()).hexdigest())

	#SHA384
	print("SHA384:\t", hashlib.sha384(s.encode()).hexdigest())

	#SHA512
	print("SHA512:\t", hashlib.sha512(s.encode()).hexdigest())


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
	user_symbols    = []
	rules = []


	# Default Generated Password
	default_rules = [default_lower, default_upper, default_num, default_symbols]
	print("This is a randomly generated 16 character password.")
	print("There are (26+26+10+30)^16 possible combinations.")
	print("That is about 2.634e31 possible combinations.")
	print("NOTE: There is a little bit less than that since the program does not allow 3 characters to repeat consecutively.")
	print_pw(pw_generator(default_rules, pw_length))
	print("===================================")


	#exit()

	# Form Submission Checks
	#  - Can be condensed into a helper function.....in later build.
	p1 = False
	p2 = False
	p3 = False
	p4 = False
	p5 = False
	p6 = False

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

	while not p2:
		allow_upper = input("Allow Upper Case (Y/N): ")
		if allow_upper[0].lower() == "y":
			allow_upper = True
			break
		elif allow_upper[0].lower() == "n":
			allow_upper = False
			break
		else:
			p2 = False
			print("\033[0;31m"+"Invalid Input. Try Again with (Y/N)"+ "\033[0m")

	while not p3:
		allow_lower = input("Allow Lower Case (Y/N): ")
		if allow_lower[0].lower() == "y":
			allow_lower = True
			break
		elif allow_lower[0].lower() == "n":
			allow_lower = False
			break
		else:
			p3 = False
			print("\033[0;31m"+"Invalid Input. Try Again with (Y/N)"+ "\033[0m")

	while not p4:
		allow_num = input("Allow Numbers (Y/N): ")
		if allow_num[0].lower() == "y":
			allow_num = True
			break
		elif allow_num[0].lower() == "n":
			allow_num = False
			break
		else:
			p4 = False
			print("\033[0;31m"+"Invalid Input. Try Again with (Y/N)"+ "\033[0m")

	while not p5:
		allow_symbols = input("Allow Symbols (Y/N): ")
		if allow_symbols[0].lower() == "y":
			allow_symbols = True
			break
		elif allow_symbols[0].lower() == "n":
			allow_symbols = False
			break
		else:
			p5 = False
			print("\033[0;31m"+"Invalid Input. Try Again with (Y/N)"+ "\033[0m")

	if allow_symbols:
		while not p6:
			print("Default Symbols: ` ! \" $ ? % ^ & * ( ) _ - + = { [ } ] : ; @ \' ~ # | \ < , > .")
			allow_default_symbols = input("Allow Default Symbols (Y/N): ")
			if allow_default_symbols[0].lower() == "y":
				allow_default_symbols = True
				break
			elif allow_default_symbols[0].lower() == "n":
				allow_default_symbols = False
				break
			else:
				p6 = False
				print("\033[0;31m"+"Invalid Input. Try Again with (Y/N)"+ "\033[0m")

	if not allow_default_symbols:
		# Note to self: Potential weakpoint where user can spam the same character
		# - Will fix in later build
		allow_symbols = input("Enter Custom Symbols, Not Characters/Numbers! (with no spaces or dividers):")
		user_symbols = list(allow_symbols)

	if not allow_lower and not allow_upper and not allow_num and not allow_symbols:
		print("You will literally have an empty string as a password.")
		print("Big mistake. Try again!")
		exit()

	# Compile User Rules:
	if allow_lower:
		rules.append(default_lower)
	if allow_upper:
		rules.append(default_upper)
	if allow_num:
		rules.append(default_num)
	if allow_symbols and allow_default_symbols:
		rules.append(default_symbols)
	elif allow_symbols and not allow_default_symbols:
		rules.append(user_symbols)

	print_pw(pw_generator(rules, pw_length))


