def quick_sort(array,p,r):
	if(p<r):
		q = partition(array,p,r)
		quick_sort(array,p,q-1)
		quick_sort(array,q+1,r)


def partition(array,p,r):
	def swap(i,j):
		temp = array[i]
		array[i] = array[j]
		array[j] = temp

	q = p
	for index in range(p,r): # p to r-1
		if array[index] < array[r]:
			swap(index,q)
			q += 1 
			# if u dont increase value of q it will be a descending sort
	swap(q,r)
	return q

	
array = [1,2,3,4,0,-1,-2,-3,-4]
print array
quick_sort(array,0,len(array)-1)

print array
