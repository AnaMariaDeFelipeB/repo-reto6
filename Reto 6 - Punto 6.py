def contigiadosEnNuncaLandia (C:int, D:int) ->int: 
    funcionExponencial = C*(2**D)
    return funcionExponencial

if __name__ == "__main__":
    C= int(input("Ingrese población de NuncaLandia infectada actualmente: "))
    D= int(input("Ingrese días a partir de hoy: "))
    poblacionInfectadaFinal = contigiadosEnNuncaLandia(C,D)
    print("Partiendo de", C, "contagiados después de", D, "días habrá un total de", poblacionInfectadaFinal, "contagiados")