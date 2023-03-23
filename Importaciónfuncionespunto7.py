from funcionespunto7 import *


if __name__ == "__main__": 
    a = float(input("Ingrese número 1: "))
    b = float(input("Ingrese número 2: "))
    c = float(input("Ingrese número 3: "))
    d = float(input("Ingrese número 4: "))
    e = float(input("Ingrese número 5: "))

    primero = funcionPromedio (a,b,c,d,e)
    segundo = funcionMediana (a,b,c,d,e)
    tercero = funcionPromedioMultiplicativo (a,b,c,d,e)
    cuarto = funcionValorMax (a,b,c,d,e)
    quinto = funcionValormin (a,b,c,d,e)
    sexto = funcionPotenciadelMayorAlMenor (a,b,c,d,e)
    septimo = funcionRaizCubicaMenor (a,b,c,d,e)
    print("Los números digitados fueron", a, ",", b,",",c,",",d,",",e)
    print("El promedio es", primero)
    print("La mediana es", segundo)
    print("El promedio multiplicativo es", tercero)
    print("El número mayor es", cuarto)
    print("El número menor es", quinto)
    print("La potencia del número al mayor es", sexto)
    print("La raíz cubica del número menor es", septimo)