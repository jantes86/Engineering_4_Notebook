#Calculator (Mr. Modulo)
#James O'Brien and Jack Antes

a = input('First number, please, Sir: ')
b = input('Second number, as well, if you would be so kind: ')


def doMath(x,y,z):
    if z == 1:
        sum = float(a) + float(b)
        sum = str(round(sum, 2))
        return sum
    if z == 2:
        difference = float(a) - float(b)
        difference = str(round(difference, 2))
        return difference
    if z == 3:
        product = float(a) * float(b)
        product = str(round(product, 2))
        return product
    if z == 4:
        quotient = float(a) / float(b)
        quotient = str(round(quotient, 2))
        return quotient
    if z == 5:
        modulo = float(a) % float(b)
        modulo = str(round(modulo, 2))
        return modulo
print("Sum:\t\t" + doMath(a,b,1))
print("Difference:\t" + doMath(a,b,2))
print("Product:\t" + doMath(a,b,3))
print("Quotient:\t" + doMath(a,b,4))
print("Modulo:\t\t" + doMath(a,b,5))
