import math
pi = math.pi
def volumenYAreaEsfera (r1:float) ->float:   #Función para definir Volumen y Area de una esfera. 
    volumenEsfera = ((3/4)*pi)*(r1**3)  
    areaEsfera = (4*pi)*(r1**2)
    return (volumenEsfera, areaEsfera)

def volumenYAreaCono (r2:float, h:float) -> float:   #Función para definir Volumen y Area de un cono. 
    slantCuadrado = (h**2)+(r2**2)
    slantFinal = slantCuadrado**0.5
    volumenCono = (1/3)*h*pi*(r2**2)
    areaCono = (pi*r2*slantFinal)+(pi*(r2**2))
    return (volumenCono, areaCono)

if __name__ == "__main__": 
    r1 = float(input("Ingrese radio de la esfera (r1): "))
    r2 = float(input("Ingrese radio del cono (r2): "))
    h = float(input("Ingrese altura del cono (h): "))
    esfera = volumenYAreaEsfera (r1)
    cono = volumenYAreaCono (r2, h)
    print("El volumen y area de la esfera es", esfera, "respectivamente. Y el volumen y area del cono es", cono, "respectivamente.") 