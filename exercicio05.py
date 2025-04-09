contDentro = 0
contFora = 0

for i in range (10):
    num = float(input("Digite um valor: "))
    if num >= 10 and num <= 20:
        contDentro = contDentro + 1
    else:
        contFora = contFora + 1

print(f"{contDentro} valores estão dentro do intervalo entre 10 e 20"
      f"\n{contFora} valores estão fora do intervalo entre 10 e 20")