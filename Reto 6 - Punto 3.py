def totalCantidadCarneAves (N:int, M:int, K:int) ->int: 
    pesoGallinas = 6 
    pesoGallos = 7 
    pesoPollitos = 1 
    cantidadCarne = (N*pesoGallinas)+(M*pesoGallos)+(K*pesoPollitos)
    return cantidadCarne

if __name__ == "__main__":
    N= int(input("Ingrese cantidad de gallinas: "))
    M= int(input("Ingrese cantidad de gallos: "))
    K= int(input("Ingrese cantidad de pollitos: "))
    totalcarne = totalCantidadCarneAves(N, M, K)
    print("La cantidad de carne de aves en kilos es", totalcarne)