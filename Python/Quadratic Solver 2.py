#Quadratic Formula Solver 2.0 Electric Bungalo
#Jack O'Brien and James Antes

import math

a = input('Given me mine A: ')
b = input('Danke schön, for that A good sir. If you would given a B, please: ')
c = input('mmmMMmMMmM. Delicious B. Gut. Now a C for desserten: ')

a=int(a)
b=int(b)
c=int(c)

def solve(x,y,z):
    discriminant = ((b**2) - (4*a*c))
    if discriminant >= 0:
        root1 = ((-b + math.sqrt(b**2 - 4*a*c))/(2*a))
        root2 = ((-b - math.sqrt(b**2 - 4*a*c))/(2*a))
        root=[root1,root2]
        return root

print('Die roots:\t' + str(solve(a,b,c)))
