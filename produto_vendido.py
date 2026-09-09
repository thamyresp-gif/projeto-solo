

#produto mais vendido

vendas_dia = ["camiseta", "calça", "camiseta", "boné", "camiseta", "calça", "boné", "camiseta"]

camisetas = input("Qual produto deseja verificar: ")

contador = 0

for vendas in vendas_dia: 
    if vendas == camisetas:
        contador += 1


print("O produto", camisetas, "foi vendido", contador, "vezes hoje.")