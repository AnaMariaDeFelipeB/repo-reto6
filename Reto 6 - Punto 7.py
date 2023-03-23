import statistics

def funcionPromedio (a:float, b:float, c:float, d:float, e:float) ->float: 
    promedio = (a+b+c+d+e)/5
    return promedio

def funcionMediana (a:float, b:float, c:float, d:float, e:float) ->float:
    mediana = statistics.median ([a, b, c, d, e])
    return mediana

def funcionPromedioMultiplicativo (a:float, b:float, c:float, d:float, e:float) ->float:
    promedioMultiplicativo = (a*b*c*d*e)**0.2
    return promedioMultiplicativo


def funcionValorMax (a:float, b:float, c:float, d:float, e:float) ->float: 
    if a>b and a>c and a>d and a>e: 
        mayor = a
    elif b>a and b>c and b>d and b>e: 
        mayor = b
    elif c>a and c>b and c>d and c>e: 
        mayor = c
    elif d>a and d>b and d>c and d>e: 
        mayor = d
    elif e>a and e>b and e>c and e>d: 
        mayor = e
    return mayor 

def funcionValormin (a:float, b:float, c:float, d:float, e:float) ->float:
    if a<b and a<c and a<d and a<e: 
        menor = a
    elif b<a and b<c and b<d and b<e: 
        menor = b
    elif c<a and c<b and c<d and c<e: 
        menor = c
    elif d<a and d<b and d<c and d<e: 
        menor = d
    elif e<a and e<b and e<c and e<d: 
        menor = e
    return menor

def funcionPotenciadelMayorAlMenor (a:float, b:float, c:float, d:float, e:float) ->float:
    if a>b and a>c and a>d and a>e: 
        mayor = a
    elif b>a and b>c and b>d and b>e: 
        mayor = b
    elif c>a and c>b and c>d and c>e: 
        mayor = c
    elif d>a and d>b and d>c and d>e: 
        mayor = d
    elif e>a and e>b and e>c and e>d: 
        mayor = e
        
    if a<b and a<c and a<d and a<e: 
        menor = a
    elif b<a and b<c and b<d and b<e: 
        menor = b
    elif c<a and c<b and c<d and c<e: 
        menor = c
    elif d<a and d<b and d<c and d<e: 
        menor = d
    elif e<a and e<b and e<c and e<d:
        menor = e 

    potenciaDelMayorAlMenor = mayor**menor
    return potenciaDelMayorAlMenor

def funcionRaizCubicaMenor (a:float, b:float, c:float, d:float, e:float) ->float:     
    if a<b and a<c and a<d and a<e: 
        menor = a
    elif b<a and b<c and b<d and b<e: 
        menor = b
    elif c<a and c<b and c<d and c<e: 
        menor = c
    elif d<a and d<b and d<c and d<e: 
        menor = d
    elif e<a and e<b and e<c and e<d:
        menor = e 
    
    raizCubicaDelMenor = menor**(1/3)
    return raizCubicaDelMenor


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