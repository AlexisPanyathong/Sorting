# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        
        # Make a for method: 
        for e in range(i + 1, len(arr)):
            # if array of e is less than (<)the array of smallest_index then smallest_index is equal to e.
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
    # Set index and count to 0.
    index = 0
    count = 0
    
    # Use a while loop
    while True:
        count = 0
        for num in range(0, len(arr) - 1):
            if arr[num] > arr[num + 1]:
                value = arr[num]
                arr[num + 1]
                arr[num + 1] = value
                count += 1
        if count == 0:
            False
            break
        
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr