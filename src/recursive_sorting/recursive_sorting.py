# TO-DO: complete the helpe function below to merge 2 sorted arrays

def merge( arrA, arrB ):

    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements

    # TO-DO


    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION

def merge_sort( arr ):

    # TO-DO
    # print( "ARRAY!" , arr )
    # RETURNS [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

    if len( arr ) == 0:
        return arr
    pivot = arr[ 0 ]
    pivots = [ x for x in arr if x == pivot ]
    small = merge_sort( [ x for x in arr if x < pivot ] )
    large = merge_sort( [ x for x in arr if x > pivot ] )
    print( small + pivots + large )

    # RETURNS [
# 0]
# [3]
# [2, 3]
# [2, 3, 4]
# [7]
# [6, 7]
# [9]
# [6, 7, 8, 9]
# [4, 2, 3, 5, 8, 9, 6, 7]
# [0, 1, 5, 8, 4, 2, 9, 6, 3, 7]

            

    return arr
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