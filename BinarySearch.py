import math

numberslist = range(0,1000)
global iterations

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

find(500)


