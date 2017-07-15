# recursive power of a number to the power of integer

from sys import argv

script, x_str , n_str  = argv

def power(x,n):
	if n == 0 : return 1
	elif n < 0 : return 1/power(x,-n)
	elif n %2 == 0 : 
		x = power(x,n/2) 
		return x*x
	else :return x*power(x,n-1) -

x = int(x_str)
n = int(n_str)

print "the value of %d to the power of %d is: "% (x,n) ,
print  power(x,n)