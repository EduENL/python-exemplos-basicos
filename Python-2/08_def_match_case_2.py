sabor = input("Indique o sabor: ")

# Função para selecionar sabor
def sabor_pizza(sabor):
    match sabor:
        case 1:
            print("Mussarela.")
        case 2:
            print("Calabrasa.")
        case 3:
            print("Frango c/ catupiry.")
        case 4:
            print("Portuguesa.")
        case _:
            print("Sabor inválido!")