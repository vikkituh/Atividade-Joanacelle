a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

print("Soma:", a + b)

if a > b:
    print("Maior:", a)
elif b > a:
    print("Maior:", b)
else:
    print("São iguais")
