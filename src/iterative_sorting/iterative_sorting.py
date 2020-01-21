# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for e in range(i + 1, len(arr)):
            if arr[e] < arr[smallest_index]:
                smallest_index = e     

        # TO-DO: swap
        elem1 = arr[i]
        elem2 = arr[smallest_index]
        arr[i] = elem2
        arr[smallest_index] = elem1

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    bubbles = len(arr)
    
    for i in range(bubbles):
        for e in range(0, bubbles-i-1):
            if arr[e] > arr[e+1]:
                arr[e], arr[e+1] = arr[e+1], arr[e]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr