import math

numberslist = range(0,1000)
global iterations
# binarysearch using recursion
def findInRange(key,numbers,i,j,n):
	middle=int((i+j)/2)
	n = n+1
	if key == numbers[middle]:
		return numbers[middle],n
	elif key < numbers[middle]:return findInRange(key,numbers,i,middle,n)
	else:return findInRange(key,numbers,middle,j,n)

def find(key):
	i = findInRange(key,numberslist,0,len(numberslist),0)
	print "found it at position :"+ str(i[0]) +"with recursion of :" + str(i[1])

# find(999)


# binary search with while loop and less variables and used it in prime numbers

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]

def is_prime(num,count):
	i = 0
	j = len(primes)
	while (j>=i):
		count = count + 1 
		guess = (i+j)/2	
		if primes[guess] == num:
			return guess,count
		elif primes[guess] > num:
			j = guess -1
		else:i = guess +1
	return None,count

prime_pos = is_prime(22,0)

print "found "+ str(prime_pos[0]) +" with recursion of :" + str(prime_pos[1])




