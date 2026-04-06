a = int(input("Digite um número inteiro: "))

if a > 0:
    if a < 10:
        print("Pequeno")
    elif a <= 100:
        print("Médio")
    else:
        print("Grande")
else:
    print("Negativo ou zero")