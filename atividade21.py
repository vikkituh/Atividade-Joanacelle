a = int(input("Digite um número inteiro: "))

if a > 0:
    if a % 2 == 0 and a % 3 == 0:
        print("Múltiplo de 2 e 3")
    else:
        print("Não atende")
else:
    print("Número inválido")