numeros = []

for i in range (4):
    while True:
        num = float(input(f"Informe o seu número {i+1}: "))
        if num <= 10:
            numeros.append(num)
            break
        else:
            print("Número inválido! Insira um número de 1 a 10")
resultado = sum(numeros) / 4
print(f"A média foi {resultado}")