valor = input("Digite um valor: ")

print("Tipo da variável:", type(valor))

try:
    num = float(valor)
    print("Resultado da divisão por 2:", num / 2)
except:
    print("Não numérico")