while True:
    num = int(input("Informe qual tabuada deseja: "))
    print(" ")
    print(f"Tabuado do {num}")
    print(" ")

    for i in range (1, 11):
        result = num * i
        print(f"{num} * {i} = {result}")
        i += 1

    continuar = input("\nDeseje calcular outra tabuada (s/n) ?")
    if continuar.lower() != 's':
        print("Encerrando o programa.")
        break