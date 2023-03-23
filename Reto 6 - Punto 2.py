import math
pi = math.pi
def perimetroYAreaRectangulo (a:float, b:float) ->float: 
    perímetroRectangulo = (2*a)+(2*b)
    areaRectangulo = a*b
    return perímetroRectangulo, areaRectangulo

def perimetroYAreaCirculo (r:float) ->float: 
    perimetroCirculo = 2*pi*r
    areaCirculo = pi*(r**2)
    return perimetroCirculo, areaCirculo

if __name__ == "__main__":
    a = float(input("Ingrese largo del rectangulo (a): "))
    b = float(input("Ingrese ancho del rectangulo (b): "))
    r = float(input("Ingrese radio del circulo (r): "))
    rectangulo = perimetroYAreaRectangulo(a, b)
    circulo = perimetroYAreaCirculo(r)
    print("El perímetro y area del rectangulo es", rectangulo, "respectivamente. Y el perímetro y area del circulo es", circulo, "respectivamente.")