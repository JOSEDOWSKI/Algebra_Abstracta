from Componentes.miller_rabin import miller_rabin
from Componentes.generan_prim import generan_prim

def Todos_primos():
    listaNum = [3,4,5]
    for i in listaNum:
        print(f"\nNúmeros primos de {i} digitos:")
        numero = (10**(i-1))
        while(numero <= (10**i)):
            if miller_rabin(numero,50):
                print(numero,end="/")
            numero += 1
    print("\n")

def todos_ran_primos():
    source = [ 
        16, 16, 16, 16, 16, 16, 16, 16, 16, 16,
        32, 32, 32, 32, 32, 32, 32, 32, 32, 32,
        64, 64, 64, 64, 64, 64, 64, 64, 64, 64
    ]

    for i in source:
        prime = generan_prim(i)
        print("{0}bits => {1}".format(i, prime))

def main():
    Todos_primos()
    todos_ran_primos()

main()