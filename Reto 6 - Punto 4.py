def vueltasTienda (P:int, M:int, H:int, B:float) ->float:
    costoPanes = P*300
    costoLeche = M*3300
    costoHuevos = H*350 
    CostoTotal = costoPanes+costoLeche+costoHuevos
    loQueMeSobra = B-CostoTotal
    return loQueMeSobra


if __name__ == "__main__":
    P= int(input("Ingrese total panes a comprar: "))
    M= int(input("Ingrese total leches a comprar: "))
    H= int(input("Ingrese total huevos a comprar: "))
    B= int(input("Ingrese valor del billete con el que pago: "))
    resultado = vueltasTienda(P, M, H, B)
    print("Lo que le sobra (o debe) es", resultado, ", si paga con un billete de", B)