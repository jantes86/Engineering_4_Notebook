#Quadratic Formula Solver
#Jack Antes and James O'Brien

import math

a = input('Given me mine A: ')
b = input('Danke schon, for that A good sir. If you would given a B, please: ')
c = input('mmmMMmMMmM. Delicious B. Gut. Now a C for desserten: ')

a=int(a)
b=int(b)
c=int(c)

discriminant = ((b^2) - (4*a*c))
if discriminant >= 0:
    root1 = ((-b + math.sqrt(b**2 - 4*a*c))/(2*a))
    root2 = ((-b - math.sqrt(b**2 - 4*a*c))/(2*a))
    root=[root1,root2]
    print('Das roots be:\t' + str(root))
else:
    print('No real roots, mein herr!')
