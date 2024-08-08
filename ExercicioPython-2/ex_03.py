nome = input("Informe o usuário: ")
senha = input("Informe a senha: ")


if nome == "admin" and senha == "1234":
    print("Acesso liberado!")
else:
    print("Acesso negado! Usuário ou senha errados.")