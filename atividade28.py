valor = input("Digite um valor: ")

try:
    if "." in valor:
        num = float(valor)
        print("Metade:", num / 2)
    else:
        num = int(valor)
        print("Dobro:", num * 2)
except:
    print("Tipo inválido")