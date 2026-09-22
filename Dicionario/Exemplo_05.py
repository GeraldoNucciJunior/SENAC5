import os
os.system('cls' if os.name == 'nt' else 'clear')

def somar(valor1=0, valor2=0):
    total = valor1 + valor2
    return total

def dividir(valor1=0, valor2=0):
    total = valor1/  valor2
    return total

def multiplicar(valor1=0, valor2=0):
    total = valor1*  valor2
    return total

def subtrair(valor1=0, valor2=0):
    total = valor1-  valor2
    return total


def FuncaoRecursiva(valor):
    valor =valor -1
    if valor == 0:
        return 1
    else:
         valor = FuncaoRecursiva(valor )
    if valor == 1:
        return 1

    


#FuncaoRecursiva(4)




valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))




print (somar(valor1, valor2))
print (dividir(valor1, valor2))
print (multiplicar(valor1, valor2))
print (subtrair(valor1, valor2))

