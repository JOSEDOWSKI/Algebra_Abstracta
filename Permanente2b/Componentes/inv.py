from Componentes.euclides import EUCLIDES_EXTEND

def INV(a, n):
    (mcd, x, y) = EUCLIDES_EXTEND(a, n)
    if mcd == 1:
        return x % n
    else:
        return None
