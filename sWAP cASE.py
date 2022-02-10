# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to
# uppercase letters and vice versa
import string

def swap_case(s):
    newlist = [ ]
    for i in range(len(s)):
        if (s[ i ] in string.ascii_lowercase ):
            newlist.append(s[ i ].upper())
        else :
            newlist.append(s[ i ].lower())
    return ( '' . join ( newlist ) )

if __name__ == '__main__':
    s = input( )
    result = swap_case(s)
    print(result)
