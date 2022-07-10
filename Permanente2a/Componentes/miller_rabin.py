import random
import math
from Componentes.POW_MOD import POW_MOD
from Componentes.comp_rand import comp_rand
import random


def compuesto(a, n, t, u):
    x = POW_MOD(a, u, n)

    if (x == 1 or x == n - 1):
        return False

    for i in range(1,t,1):
        x = POW_MOD(x, 2, n)
        if (x == n - 1):
            return False

    return True

def miller_rabin(n, s):
    t = 0
    u = n - 1
    while (u % 2 == 0):
        u = u / 2
        t = t + 1

    j = 1
    while (j < s):
        a = comp_rand(2, n - 1)
        if (compuesto(a, n, t, u)):
            return False
            
        j += 1

    return True