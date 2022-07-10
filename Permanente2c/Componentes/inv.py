from Componentes.euclides import Euclides_E

def INV(a, n):
    (mcd, x, y) = Euclides_E(a, n)
    if mcd == 1:
        return x % n
    else:
        return None