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
