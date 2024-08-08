valor = int(input("Informe o valor: "))

alerta = "Situação normal" if valor < 100 else "Situação: Pré-diabetes" if valor in range(100, 125) else "Situação: Diabetes"

print(alerta)