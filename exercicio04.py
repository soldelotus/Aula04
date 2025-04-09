cont = 0

for i in range (1, 10, 1):
    num = float(input("Digite um valor: "))
    if num < 0:
        cont = cont + 1

print(f"A quantidade de números negativos é {cont}")