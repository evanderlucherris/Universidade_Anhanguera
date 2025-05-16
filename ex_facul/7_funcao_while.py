numero = int(input('Insira um número: '))

while numero != 0:

    if numero % 2 == 0:
        print('Este número é par!')
        numero = int(input())
    else:
        print('Este número é ímpar!')
        numero = int(input())