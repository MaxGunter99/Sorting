import os
os.system( 'clear' )

# TO-DO: Complete the selection_sort() function below 

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7 ]

def selection_sort( arr ):
    # loop through n-1 elements

    sorted_values = []

    print( 'start' , arr[0]  )

    sorted_values.append( arr[0] )

    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             
        


        # TO-DO: swap

        if arr[ i ] > sorted_values[ len( sorted_values ) - 1 ]:
            sorted_values.append( arr[ i ] )
            print( arr[ i ] )

        elif arr[ i ] <  sorted_values[ len( sorted_values ) - 1 ]:
            
            # INSERT FORMAT: arr.insert( index , element )
            print( '----------' )
            for x in range( len( sorted_values ) - 1 ):
                
                if arr[ i ] < sorted_values[ x ]:

                    print( 'Sorted' , sorted_values )
                    print( f'{arr[ i ]} < { sorted_values[ x ] } , should insert at { x }' ) 

                    sorted_values.insert( x , arr[ i ] )
                    break
            

    print( 'Sorted_values:' , sorted_values )
    return arr

selection_sort( arr1 )


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr