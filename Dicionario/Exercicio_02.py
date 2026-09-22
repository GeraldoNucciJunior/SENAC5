import os
os.system('cls' if os.name == 'nt' else 'clear')

def dobrar(valor1,valor2,valor3):
    print (valor1 *2)
    print (valor2 *2)
    print (valor3 *2)



valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))

dobrar(valor1,valor2,valor3)