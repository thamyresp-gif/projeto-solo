
#estoque de produtos

qtd_estoque = [15, 3, 0, 22, 7, 0, 1]

total_estoque = 0

produtos_falta = 0

estoque_baixo = 0

for estoque in qtd_estoque:
    total_estoque += estoque

    if estoque == 0:
        produtos_falta += 1

    elif 1 <= estoque <= 5:
        estoque_baixo += 1


print(f"Total de estoque: {total_estoque}")
print(f"Produtos em falta: {produtos_falta}")
print(f"Estoque baixo: {estoque_baixo}")
            


