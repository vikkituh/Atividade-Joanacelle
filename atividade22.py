valor = input("Digite um valor: ")

try:
    a = int(valor)
    if a > 10:
        print("Alto")
    else:
        print("Baixo")
except:
    print("Entrada inválida")