# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 

        for j in range( i + 1 , len( arr ) ):
            if arr[ smallest_index ] > arr[ j ]:
                smallest_index = j
        
        # TO-DO: swap

        temp = arr[ cur_index ]
        arr[ cur_index ] = arr[ smallest_index ]
        arr[ smallest_index ] = temp



    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    for i in range( len( arr ) ):
        for t in range( len( arr ) - 1 ):
            if arr[ t ] > arr[ t + 1 ]:
                temp = arr[ t ]
                arr[ t ] = arr[ t + 1 ]
                arr[ t + 1 ] = temp

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

# RUN IN TERMINAL | python3 iterative_sorting.py |
# TEST WITH | python3 test_iterative.py |