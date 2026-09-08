
#relatório de vendas

vendas = [1200, 950, 1800, 0, 2200, 1100, 0, 1750, 980, 1600]

faturamento_total = 0
dias_sem_vendas = 0
media_vendas = 0
produtos_acima = 0

for venas in vendas:
    faturamento_total += venas
    if venas == 0:
        dias_sem_vendas += 1
    if venas > 1500:
        produtos_acima += 1

media_vendas = faturamento_total / len(vendas)

print("Faturamento total:", faturamento_total)
print("Média de vendas:", media_vendas)
print("Quantidade de dias sem vendas:", dias_sem_vendas)
print("Quantidade de dias com vendas acima de R$1500,00:", produtos_acima)
