# Consider a list ( list = [ ] ) . You can perform the following commands :

# insert i e : Insert integer e at position i .
# print : Print the list .
# remove e : Delete the first occurrence of integer e .
# append e : Insert integer e at the end of the list .
# sort : Sort the list .
# pop : Pop the last element from the list .
# reverse : Reverse the list .

# Initialize your list and read in the value of n followed by n lines of commands where
# each command will be of the types listed above.
# Iterate through each command in order and perform the corresponding operation on your list.
if __name__ == '__main__':
    list = [ ]
    n = int ( input ( ) )
    for i in range( n ) :
        query = input ( ) . split ( )
        if len ( query ) == 3 :
            eval ( " list . " + query [ 0 ] + " ( " + query [ 1 ] + " , " + query [ 2 ] + " ) " ) 
        elif len ( query ) == 2 :
            eval ( " list . " + query [ 0 ] + " ( " + query [ 1 ] + " ) " )
        elif ( query [ 0 ] == "print" ) :
            print ( list )
        else :
            eval ( " list . " + query [ 0 ] + " ( ) " )
