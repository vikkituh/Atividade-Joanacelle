idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Menor de idade")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")
