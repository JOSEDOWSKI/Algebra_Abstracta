from Componentes.miller_rabin import miller_rabin
from Componentes.comp_rand import comp_rand

def BITS_R(b):
    max = pow(2, b) - 1
    n = comp_rand(0, max)
    m = pow(2, b - 1) + 1
    n = n | m

    return n

def generan_prim(b):
    configure_s = 40
    s = configure_s
    n = BITS_R(b)
    while (not miller_rabin(n, s)):
        n += 2
  
    return n