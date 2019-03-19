def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
	n = len(items)
 
    # Traverse through all array elements
	for i in range(n):
 
        # Last i elements are already in place
		for j in range(0, n-i-1):
            if items[j] > items[j+1] :
                items[j], items[j+1] = items[j+1], items[j]
    return items

def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
    len_i = len(items)
    # Base case. A list of size 1 is sorted.
    # Cae returns, so if reached then function will terminate after line 8
    if len_i == 1:
        return items
    # Recursive case. Find midpoint of list
    mid_point = int(len_i / 2)
    # divide list into two halves
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])
    # call merge_sort function on each half of list 
    return merge(i1, i2)

# Merge function.
def merge(A, B):
    new_list = []
    while len(A) > 0 and len(B) > 0:
        if A[0] < B[0]:
            new_list.append(A[0])
            A.pop(0)
        else:
            new_list.append(B[0])
            B.pop(0)

    if len(A) == 0:
        new_list = new_list + B
    if len(B) == 0:
        new_list = new_list + A

    return new_list

def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    if len(items) < 2:
        return items
    else:
        pivot = items[0]
        less = [i for i in items[1:] if i <= pivot]
        greater = [i for i in items[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)