valor = input("Digite um valor: ")

try:
    a = int(valor)
    if a % 2 == 0:
        if a > 100:
            print("Par alto")
        else:
            print("Par baixo")
    else:
        print("Ímpar")
except:
    print("Entrada inválida")