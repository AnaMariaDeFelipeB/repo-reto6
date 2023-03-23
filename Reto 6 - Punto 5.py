def calculoInteresPrestamo (C:float, i:float, n:int) ->float: 
    InteresPrestamoFinal = C*((1+(i/100))**n)
    return InteresPrestamoFinal

if __name__ == "__main__":
    C= float(input("Ingrese valor inicial del préstamo: "))
    i= float(input("Ingrese valor del interés en porcentaje (sin el simbolo %): "))
    n= int(input("Ingrese longevidad del préstamo en meses: "))
    final = calculoInteresPrestamo (C, i, n)
    print("El valor final del préstamo es", final)