numero = input("digite um número inteiro")
numero = int(numero)
a = 1
while True:
    a = a + 1
    if numero == 1:
        print("Não primo")
        break
    elif numero <= 0:
        print("Número inválido")
        break
    elif numero % a == 0 and a != numero:
        print("Não primo")
        break
    elif a == numero:
        print("Primo")
        break
