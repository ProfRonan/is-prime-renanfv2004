n = int(input())

if n <= 0:
    print("Número inválido")
else:
    if n == 1:
        print("Não primo")
    else:
        i = 2
        while i < n:
            if n % i == 0:
                print("Não primo")
                break
            i += 1
        else:
            print("Primo")
