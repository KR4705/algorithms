
# recursive mergesort 
def merge_sort(array,p,r):
    if p<r:
        q = (p+r)/2
        merge_sort(array,p,q)
        merge_sort(array,q+1,r)
        merge(array,p,q,r)

def merge(array,p,q,r):
    lowHalf = array[p:q+1] 
    # array[a:b] implies it includes 
    # key a but not b the above goes from p to q
    upHalf = array[q+1:r+1] # keys from q+1 to r 
    print lowHalf,upHalf
    i = 0
    j = 0
    k = p
    while (i < len(lowHalf) and j < len(upHalf)):
        if lowHalf[i] < upHalf[j] :
            array[k] = lowHalf[i]
            i = i+1
        else: 
            array[k] = upHalf[j]
            j = j+1
        k = k +1

    while (i < len(lowHalf)):
        array[k] = lowHalf[i]
        i = i+1
        k = k +1

    while (j < len(upHalf)):
        array[k] = upHalf[j]
        j = j+1
        k = k+1

array = [0,1,2,3,4,5,6,7,8]
def sort(array):
    print array
    merge_sort(array,0,len(array)-1)
    print array

sort(array)
