i = 1
while i <= 3:-

    user = input("Informe o usupario: ")
    senha = input("Informe a senha: ")

    if user != "Gisele" and senha != "123":
        i += 1
        print("Usuário ou senha incorretos!")
        print(" ")
    else:
        print(" ")
        print(f"Bem-vindo, {user}!")
        break
else:
    print("Você excedeu o limite de tentativas")