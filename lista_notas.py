
#lista de notas 

notas = [7.5, 8.0, 5.5, 9.0, 4.0, 6.5]

soma = 0
aprovados = 0
reprovador = 0

for nota in notas:
    soma += nota
    if nota >= 6.0:
        aprovados += 1
    else:
        reprovador += 1

media = soma / len(notas)

print("Média das notas:", media)
print("Quantidade de aprovados:", aprovados)
print("Quantidade de reprovados:", reprovador)





