# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen .

def split_and_join ( line ) :
    line = line . split ( " " ) 
    result = "-" . join ( line )
    return result

if __name__ == '__main__':
    line = input( )
    result = split_and_join( line )
    print( result )
