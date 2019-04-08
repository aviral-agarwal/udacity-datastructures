"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    '''user calls this simple function'''
    recursiveFxn(array,0,len(array)-1)
    return array
    
def recursiveFxn(array,low,high):
	'''this is the function which will be called recursively'''
	if low < high:
		p = partition(array,low,high)
		recursiveFxn(array,low,p - 1)
		recursiveFxn(array,p + 1,high)

def partition(array,low,high):
	'''does the main work of quick sort'''
	pivotIndex = getPivot(array,low,high)
	pivotValue = array[pivotIndex]
	array[pivotIndex],array[low] = array[low],array[pivotIndex]
	border = low

	for i in range(low,high+1):
		if array[i] < pivotValue:
			border += 1
			array[i],array[border] = array[border],array[i]
	array[low],array[border] = array[border],array[low]
	return border