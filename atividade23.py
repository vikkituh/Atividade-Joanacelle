a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

resto = [a % 3, b % 3, c % 3]
resto.sort(reverse=True)

print("Resto em ordem decrescente:", resto)