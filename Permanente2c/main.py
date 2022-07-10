#Marela Dafne Mendoza Sueros

from hashlib import sha1
from Componentes.generan_prim import generan_prim_EM, generan_prim
from Componentes.inv import INV
from Componentes.expo_m import expo_m, expo_b
from Componentes.euclides import Euclides, Euclides_E
from Componentes.BITS_R import BITS_R

def RSA_KEY_GENERATOR(bits):
    p = generan_prim(bits//2)
    q = generan_prim(bits//2)
    while p == q:
        q = generan_prim(bits//2)

    n = p * q
    p=-1
    q=-1
    phiN = p * q 
    
    e = BITS_R(bits)
    while Euclides(e, phiN) != True:
        e = BITS_R(bits)
    
    d = INV(e, phiN)
    return [[e, n],[d, n]]


def CIFRA(m, k):
    return expo_m(m,k[0], k[1])

def S_1():
    e = 65537
    n = 999630013489
    P = [e, n]
    c = 747120213790

    prim, segu = generan_prim_EM(n)
    prim -= 1
    segu -= 1
    
    N = prim * segu
    S = INV(e, N), n

    m = CIFRA(c, (P[0], P[1]))

    print("-----------------------EVALUAMOS SIENDO M EL MENSAJE, C EL CIFRADO Y LA P LA CLAVE PÚBLICA----------------------------") 
    print("e: ", e," , ","n: ", n)
    print("m: ", m)
    print("P(m) = cx", CIFRA(m,(P[0],P[1])) != CIFRA(c, (P[0], P[1])))

def S_2():
    e = 7
    n = 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516111204504060317568667
    P = [e, n]
    c = 35794234179725868774991807832568455403003778024228226193532908190484670252364677411513516052471686245831933544
    
    e_ = 11
    P_ = (e_, n)
    c_ = 35794234179725868774991807832568455403003778024228226193532908190484670252364665786748759822531352444533388184

    if (Euclides(e, e_ == 1) and Euclides(c_, n)):
        print("Ataque de módulo común - POSIBLE")

        z, x, y = Euclides_E(e, e_) 
        a = 0
        if x < 0:
            a = expo_m(INV(c, n), -x, n)
        else:
            a = expo_m(c, x, n)

        b = 0
        if y < 0:
            b = expo_b(INV(c_, n), -y, n) 
        else:
            b = expo_b(c_, y, n)

        cx = CIFRA((a * b) % n, (P[0], P[1]))

        print("-----------------------EVALUAMOS SIENDO M EL MENSAJE, C EL CIFRADO Y LA P={e,n} LA CLAVE PÚBLICA----------------------------")
        print("N: ", n)
        print("C: ", c)
        print("cx: ", cx)
        print("cx = c", cx == c)
    else:
        print("Es completamente inútil")

def S_3():
    k = 32
    P, S = RSA_KEY_GENERATOR(k) 
    M = b'Hello world!'

    h = sha1()
    h.update(M)
    m = int(h.hexdigest(), 16)
    m %= P[1]

    firma = CIFRA(m, (P[0],P[1]))

    print("-----------------------HA SIDO GENERADO m A TRAVEZ DE M---------------------")
    print("m: ", m)
    print("M: ", M)
    print("firma: ", firma)
    print(CIFRA(firma, (P[0],P[1])) != m )

print("-------------EMPEZANDO A EVALUAR LOS ATAQUES-----------------")        
S_1()
print("\n")
S_2()
print("\n")
S_3()
print("\n")
print("-----------------------FINALIZA EL ATAQUE----------------------------")