# SelectionSort.py
# swaps the values of two keys i and j
def swap(array,i,j):
	temp = array[i]
	array[i] = array[j]
	array[j] = temp
#assuming the array is sorted till the index i, we find the
#index of the smallest value with index greater than i
def minIndexOfSubarray(array,i):
	minValue = array[i]
	minIndex = i
	for index in range(i,len(array)): # range(n) implies 0 to n-1
		if array[index] < minValue:
			minValue = array[index]
			minIndex = index
	return minIndex
#loop over the array and for each index we find the min index of subarray and swap it with the current index.
def selectionSort(array):
	for index in range(len(array)): 
		swap(array,index,minIndexOfSubarray(array,index))
	return None

array = [ 2, 5, -2, 6, -3, 8, 0, -7, -9, 4]

print array , " sorting .... "
selectionSort(array)
print array

# comments 
# asymptotic analysis
# swap irrespective of the array size runs 3 statements i.e Teta(1)
# minIndexOfSubarray (n-i) times a Teta(1) computation in forloop
# selectionSort calls minIndexOfSubarray n times with i looping from 0 to n-1
# implies n + n-1 + n-2 + ..... +1 
#  n/2(n+1) i.e Teta(n^2) 
