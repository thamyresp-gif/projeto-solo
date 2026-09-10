
#ANALISE DE VENDAS 


vendas = [
    {"produto": "Tênis", "categoria": "Calçados", "quantidade": 3, "preco": 250},
    {"produto": "Camiseta", "categoria": "Roupas", "quantidade": 5, "preco": 80},
    {"produto": "Tênis", "categoria": "Calçados", "quantidade": 2, "preco": 300},
    {"produto": "Calça", "categoria": "Roupas", "quantidade": 4, "preco": 150},
    {"produto": "Boné", "categoria": "Acessórios", "quantidade": 6, "preco": 50},
    {"produto": "Camiseta", "categoria": "Roupas", "quantidade": 3, "preco": 90},
]

tenis = 0
camiseta = 0
calca = 0
bone = 0

for produto in vendas:

   if produto["produto"] == "Tênis":
    tenis += produto["quantidade"]

   elif produto["produto"] == "Camiseta":
     camiseta += produto["quantidade"]

   elif produto["produto"] == "Calça":
     calca += produto["quantidade"]

   elif produto["produto"] == "Boné":
      bone += produto["quantidade"]


print("Tênis: ", tenis)
print("Camiseita: ", camiseta)
print("Calça: ", calca)
print("Boné: ", bone)
