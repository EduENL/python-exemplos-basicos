def ler_informacoes():
    while True:
        nome = input("Informe seu nome: ")
        if len(nome) > 3:
            break
        print("Seu nome deve conter mais que 3 caractéres")

    while True:
        idade = int(input("Informe sua idade: "))
        if idade in range(0,100):
            break
        print("Sua idade deve estar entre 0 e 100 anos")

    while True:
        salario = float(input("Informe seu salário: "))
        if salario > 0:
            break
        print("Seu salário deve ser maior que 0")

    while True:
        sexo = input("Informe seu sexo (f/m): ").lower()
        if sexo in ['f', 'm']:
            break
        print("Gênero incorreto")

    while True:
        estado_civil = input("Informe seu estado cívil (s/c/v/d): ").lower()
        if estado_civil in ['s', 'c', 'v', 'd']:
            break
        print("Estado cívil incorreto")

    return nome, idade, salario, sexo, estado_civil  # Return the values as a tuple

nome, idade, salario, sexo, estado_civil = ler_informacoes()

print("Informações validadas:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salario:.2f}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")