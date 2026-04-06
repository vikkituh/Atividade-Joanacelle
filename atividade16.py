valor = input("Digite um valor: ")

print("Tipo:", type(valor))

try:
    a = float(valor)
    print("Quadrado:", a ** 2)
except:
    print("Não é numérico")
