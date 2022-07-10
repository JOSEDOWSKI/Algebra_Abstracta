from Componentes.inv import INV
from Componentes.generan_prim import generan_prim
from Componentes.BITS_R import BITS_R
from Componentes.euclides import Euclides
from Componentes.expo_m import expo_m

def RSA_KEY_GENERATOR(bits):
    arg = bits // 2
    p = generan_prim(arg)
    q = generan_prim(arg)
    while p == q:
        q = generan_prim(arg)

    n = p * q
    phiN = (p - 1) * (q - 1)
    
    e = BITS_R(bits)
    while Euclides(e, phiN) != 1:
        e = BITS_R(bits)
    
    d = INV(e, phiN)
    return (e, n), (d, n)

def CIFRA(m, k: tuple):
    arg1, arg2 = k
    return expo_m(m, arg1, arg2)

def main():
    k = 64
    P, S = RSA_KEY_GENERATOR(k)
    e, n = P
    d, _ = S
    print("                   VALORES SOLICITADOS                    ")


    tab = 62
    print('e = {:}\nd = {:}\nn = {:}\n'.format(e, d, n))
    print("                     TABLA DE VALORES                    ")
    print('---------------------------------------------------------')
    print('{:^20}{:^20}{:^20}'.format('m', 'c = p(m)', 'm\' = S(c)'))
    print('---------------------------------------------------------')

    stack = []
    for i in range(10):
        m = BITS_R(32)
        while m in stack:
            m = BITS_R(32)
        stack.append(m)
        c = CIFRA(m, P)
        print('{:^20}{:^20}{:^20}'.format(m, c, CIFRA(c, S)))

main()