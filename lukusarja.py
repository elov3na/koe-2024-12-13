import math

def lukusarja(alku: int) -> list:
    lista = []

    while alku != 1:
        if alku % 2 != 0:
            alku = alku * 3 + 1
        else:
            alku = alku / 2
        lista.append(math.ceil(alku))

    return lista

