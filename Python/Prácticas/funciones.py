"""def sumar ( x : int , y : int ) -> int :
    sumando : int = 0
    abs_y : int = 0

    if y < 0:
        sumando = -1
        abs_y = -y
    else :
        sumando = 1
        abs_y = y

    result : int = x
    count : int = 0

    while ( count < abs_y ):
        result = result + sumando
        count = count + 1
    return result
"""

def triangle ( a : int , b : int , c : int ) -> int :

    if ( a <= 0 or b <= 0 or c <= 0):
        return 4 # invalido

    if ( not (( a + b > c ) and ( a + c > b ) and ( b + c > a ))):
        return 4 # invalido

    if ( a == b and b == c ):
        return 1 # equilatero

    if ( a == b or b == c or a == c ):
        return 2 # isosceles

    return 3 #escaleno

print (triangle(4,8,5))
