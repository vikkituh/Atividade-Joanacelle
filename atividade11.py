a = int(input("Digite um número: "))

if a % 2 == 0 and a > 0:
    print("Par positivo")
elif a % 2 == 0 and a < 0:
    print("Par negativo")
else:
    print("Ímpar")
