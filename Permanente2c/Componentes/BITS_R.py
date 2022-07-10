from Componentes.comp_rand import comp_rand

def BITS_R(b):
    max = pow(2, b) - 1
    n = comp_rand(0, max)
    m = pow(2, b - 1) + 1
    n = n | m

    return n