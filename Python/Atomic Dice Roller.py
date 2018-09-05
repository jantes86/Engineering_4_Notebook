#Automatic Dice Roller
#Written by James O'Brien and Jack Antes

print("Welcome to the Atomic Dice Roller!") 
print("Press enter for a number between 1 and 20. Enter the letter x to make it stop.")

from random import *

repeat = True
while repeat:
    x = randint (1, 20)

    print(x)

    if ('x') in input():

        repeat = False
