num_1 = float(input("Informe o seu primeiro número: "))

if num_1 <= 10:
    num_2 = float(input("Informe o seu segundo número: "))
    if num_2 <= 10:
        num_3 = float(input("Informe o seu terceiro número: "))
        if num_3 <= 10:
            num_4 = float(input("Informe o seu quarto número: "))
            if num_4 <= 10:
                resultado = (num_1 + num_2 + num_3 + num_4)/4
                print(f"A média foi {resultado}")
            else:
                print("Número inválido")
        else:
                print("Número inválido")
    else:
                print("Número inválido")
else:
                print("Número inválido")