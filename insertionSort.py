# insertionSort.py

# insert below takes an array and the index to which it is sorted 
# and inserts the value in this sorted array
def insert(array,rightIndex,value):
	for x in range(rightIndex +1):
		if array[rightIndex-x] > value:
			array[rightIndex-x + 1] = array[rightIndex-x]
		else: 
			array[rightIndex-x+1] = value  
			return
	array[0] = value
	return	




array = range(8,-10,-2)
print "initial array:", array

def insertionSort(array):
	for index in range(len(array)-1):
		insert(array,index,array[index+1])
	return

insertionSort(array)

print "the sorted array:", array

# notes :
# not the end cases for the insertion sort.
# starting at rightindex = 0 and rightindex = n-2 ?? 
# the last element is already sorted.
# also our insert needs onemore index n
# to be able to sort at the rightindex = n-1
# which is not the case.