# palindrome_recursive.py

from sys import argv

name , string = argv

def pal(arg):
	if len(arg) == 1 or len(arg) == 0: 
		return True
	elif arg[0] == arg[len(arg)-1]:
		return pal(arg[1:len(arg)-1])
	else: return False 

print pal(string)
