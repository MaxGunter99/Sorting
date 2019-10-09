import os
import random
os.system( 'clear' )

# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):

    solution = []
    #compare ( already sorted )
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    count = 0

    # TO-DO
    index_a = 0
    index_b = 0

    while count < elements:

        print( index_a , index_b )

        if len( arrA ) <= index_a:

            solution.extend( arrB[ index_b: ] )
            break

        elif len( arrB ) <= index_b:

            solution.extend( arrA[ index_a: ] )
            break

        elif arrA[ index_a ] < arrB[ index_b ]:

            solution.append( arrA[ index_a ] )
            count += 1
            index_a += 1

        else:

            solution.append( arrB[ index_b ] )
            count += 1
            index_b += 1

    print( solution )
    return solution



# TO-DO: implement the Merge Sort function below USING RECURSION

def merge_sort( arr ):

    # SEPERATE
    pivot = len( arr ) // 2

    if arr == []:

        return []

    else:

        if len( arr ) == 1:

            return arr

        else:

            pivot = len( arr ) // 2

            left = merge_sort( arr[ :pivot ] )
            right = merge_sort( arr[ pivot: ] )

            print( 'Left:' , left , 'Right:' , right )

            section = merge( left , right )
            return section
 

            

arr1 = [ 1 , 5 , 8 , 0 , 4 , 2 , 7 , 3 ]
merge_sort( arr1 )





# def merge_sort( arr ):

#     # THIS PASSES ALL TESTS BUT I DONT THINK ITS ON THE RIGHT TRACK

#     for i in range( len( arr ) - 1):

#         if arr[ i ] > arr[ i + 1 ]:
#             print( f'{ arr[ i ] } > { arr[ i + 1 ] }' )
#             move = arr[i]
#             arr.remove( move )
#             arr.insert( i + 1 , move )
#             merge_sort( arr )

#         else:
#             print( f'{ arr[ i ] } < { arr[ i + 1 ] }' )

#     os.system( 'clear' )
    # return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
