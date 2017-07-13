from sys import argv

name,n_string = argv
n = int(n_string)
def fact(n):
	result = 1
	for index in range(2,n+1,1):
		result *= index
	return result

print "factorial of %d is > " %n ,
print fact(n)