def escolha_usuario(escolha):
    match escolha:
        case 1:
            print("Você programa em Python")
        case 2:
            print("Você programa em PHP")
        case 3:
            print("Você programa em Java")
        case _:
            print("Escolha uma opção válida!")

while True:
    print("Opção 1 - Eu programo em Python")
    print("Opção 2 - Eu programo em PHP")
    print("Opção 3 - Eu programo em Java")

    usuario_escolha = int(input("Escolha uma das opções: "))

    escolha_usuario(usuario_escolha)

    if usuario_escolha in [1, 2, 3]:
        break