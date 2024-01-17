import os
os.system("cls")


def suma (a,b):
    c = a + b
    print("La suma es a + b es: ",c)
    
def resta (a,b):
    d = a - b
    print("La resta de a - b es: ",d)
    
def multiplicacion (a,b):
    e = a * b
    print("La multiplicación de a * b es: ",e)
def division (a,b):
    if b == 0:
        print("La división no se puede hacer")
    else:
        f = a/b
        print("La division de a7b es: ",f)


suma(2,3)
resta(2,3)
multiplicacion(2,3)
division(2,0)