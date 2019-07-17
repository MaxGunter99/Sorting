# TO-DO: complete the helpe function below to merge 2 sorted arrays

def merge( arrA, arrB ):

    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    # TO-DO
    # SANITY CHECK
    print( arrA  , arrB)

    # VALUES
    left_value = 0
    right_value = 0
    index_tracker = 0

    # EVENLY DEVIDED
    while left_value < len( arrA ) and right_value < len( arrB ):
        
        if arrA[left_value] < arrB[right_value]:
            merged_arr[index_tracker] = arrA[left_value]
            left_value += 1

        else:
            merged_arr[index_tracker] = arrB[right_value]
            right_value += 1

        index_tracker += 1

    # IF ARRA HAS MORE ITEMS
    while left_value < len( arrA ):
        merged_arr[index_tracker] = arrA[left_value]
        left_value += 1
        index_tracker += 1

    # IF ARRB HAS MORE ITEMS
    while right_value < len( arrB ):
        merged_arr[index_tracker] = arrB[right_value]
        right_value += 1
        index_tracker += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION

def merge_sort( arr ):

    # IF ARRAY IS UNEVEN
    if len( arr ) <= 1:
        return arr

    # MIDDLE VALUE
    pivot_point = len( arr ) // 2

    # ALL ITEMS SMALLER/ LARGER THAN PIVOT_POINT
    shorter_array = arr[:pivot_point]
    taller_array = arr[pivot_point:]

    # READY
    shorter = merge_sort( shorter_array )
    taller = merge_sort( taller_array )

    # SET
    arr = merge( shorter , taller )

    # GO
    return arr




# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

    return arr

# RUN IN TERMINAL | python3 recursive_sorting.py |
# TEST WITH | python3 test_recursive.py |