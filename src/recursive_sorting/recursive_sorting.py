# TO-DO: complete the helpe function below to merge 2 sorted arrays

def merge( arrA, arrB ):

    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    # TO-DO


    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION

def merge_sort( arr ):

    # ARRAY
    print( "Array" , arr )

    # MIDDLE VALUE
    pivot_point = len( arr ) // 2

    # ALL ITEMS LARGER THAN PIVOT_POINT
    while len( arr ) > 2:
        taller = arr[ pivot_point: ]
        taller_pivot_point = len( taller ) // 2
        print( taller_pivot_point )

        # ALL ITEMS SMALLER THAN PIVOT_POINT
        shorter = arr[ :pivot_point ]
        shorter_pivot_point = len( shorter ) // 2
        print( shorter_pivot_point )

    return arr








# # TO-DO: complete the helpe function below to merge 2 sorted arrays

# def merge( arrA, arrB ):

#     elements = len( arrA ) + len( arrB )
#     merged_arr = [0] * elements

#     # TO-DO


#     return merged_arr

# # TO-DO: implement the Merge Sort function below USING RECURSION

# def merge_sort( arr ):

#     if len( arr ) == 0:
#         return arr

#     # starting number, comparing pivot to every other number in set
#     pivot = arr

#     pivots = [ x for x in arr if x == pivot ]

#     # decide if selected number in array is smaller than the pivot
#     shorter = merge_sort( [ x for x in arr if x < pivot ] )

#     # decide if selected number in array is larger than the pivot point
#     taller = merge_sort( [ x for x in arr if x > pivot ] )

#     # add all together, smallest to largest
#     arr = shorter + pivots + taller

#     print( arr )      

#     return arr








# STRETCH: implement an in-place merge sort algorithm
# def merge_in_place(arr, start, mid, end):
#     # TO-DO

#     return arr

# def merge_sort_in_place(arr, l, r): 
#     # TO-DO

#     return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
# def timsort( arr ):

#     return arr

# RUN IN TERMINAL | python3 recursive_sorting.py |
# TEST WITH | python3 test_recursive.py |