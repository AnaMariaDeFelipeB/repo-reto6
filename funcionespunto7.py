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