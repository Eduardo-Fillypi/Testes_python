valor_compra = float(input("Valor do carro:"))
valor_investido = float(input("Valor investido no carro:"))
valor_venda = float(input("Valor de venda do carro:"))

custo = valor_compra + valor_investido
lucro = valor_venda - custo

print("O custo do carro foi de: R$" + str(custo))
print("Você lucrou: R$" + str(lucro))
