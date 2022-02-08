#Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second
#lowest grade.
#Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

N = int(input())

students = [ ]
for i in range( 2 * N ) :
    students.append ( input ( ) . split ( ) )
grades = { }
for j in range ( 0 , len ( students ) , 2 ) :
    grades [ students [ j ] [ 0 ] ] = float ( students [ j + 1 ] [ 0 ] )
result = [ ] 
num = sorted ( set ( grades . values ( ) ) ) [ 1 ]
for pupil in grades . keys ( ) :
    if grades [ pupil ] == num :
        result . append ( pupil )
for k in sorted ( result ) :
    print (k)
