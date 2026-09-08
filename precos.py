
#carrinho de compras

precos = [25.90, 12.50, 8.00, 45.00, 15.30]

total_compra = 0
produtos_acima = 0
produto_barato = precos [0]


for preco in precos:
    total_compra += preco
    if preco > 20:
        produtos_acima += 1
    if preco < produto_barato:
        produto_barato = preco


print("Total da compra:", total_compra)
print("Quantidade de produtos acima de R$20,00:", produtos_acima)
print("Produto mais barato:", produto_barato)


