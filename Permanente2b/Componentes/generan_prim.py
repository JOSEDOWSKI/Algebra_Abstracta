from Componentes.miller_rabin import miller_rabin
from Componentes.BITS_R import BITS_R
from Componentes.euclides import Euclides

def generan_prim(b):
    configure_s = 40
    s = configure_s
    n = BITS_R(b)
    while (miller_rabin(n, s) == False):
        n += 2
  
    return n

def generan_prim_EM(n):
    primos = ()
    for i in range(1, n):
        if Euclides(i, n) != 1 and miller_rabin(i, 500):
            primos += (i,)
            if len(primos) == 2:
                break

    return primos