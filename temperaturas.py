
#lista de temperaturas em celsius

temperaturas = [28, 31, 25, 22, 30, 27, 33]

maior = temperaturas [0]
menor = temperaturas [0]
soma = 0
dias_quentes = 0
media = 0



for temp in temperaturas: 
    soma += temp
    if temp > maior:
        maior = temp
    if temp < menor:
        menor = temp
    if temp > 30:
        dias_quentes += 1
    


print("Maior temperatura:", maior)
print("Menor temperatura:", menor)  
print("Dias com temperatura acima de 30°C:", dias_quentes)
print("Média das temperaturas:", soma / len(temperaturas))
