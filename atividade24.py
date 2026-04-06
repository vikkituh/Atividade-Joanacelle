a = int(input("Digite um número inteiro: "))

if 1 <= a <= 100:
    if a % 2 == 0:
        print("Par no intervalo")
    else:
        print("Ímpar no intervalo")
else:
    print("Fora do intervalo")