# Entrada
VProduto = float(input("Insira o valor do Produto: "))
PorcentComissao = float(input("Insira a porcentagem da comissão: "))

# Calculo
Comissao = (VProduto * (PorcentComissao / 100))

# Saida
print(f"A sua comissão tem o valor de R${Comissao}")