# Raghu  is a shoe shop owner. His shop has X number of shoes. He has a list containing the size of each shoe he has in his shop.
# There are N number of customers who are willing to pay x amount of money only if they get the shoe of their desired size. 
# Your task is to compute how much money Raghu earned.

from collections import Counter
x = input( )
S = Counter(map(int,input( ).split( )))
n = input( )
N = int(n)
earnings = 0
for customer in range ( N ):
    size , x_i = map(int,input().split())
    if size in S and S[size] > 0 :
        S[size] -= 1
        earnings += x_i
print(earnings)
