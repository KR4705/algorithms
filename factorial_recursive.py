from sys import argv

name , n_string = argv
n = int(n_string)

def fact_recursive(n):
	if n == 1 or n == 0 : return 1
	elif n > 1 : return fact_recursive(n-1) * n
	else : print "Wrong argument for factorial"

print "factorial of %d is: %d" % (n,fact_recursive(n))