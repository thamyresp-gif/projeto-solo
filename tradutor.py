
#Desafio: Tradutor de "Manês"
#Escreva uma função que recebe uma frase e troca todas as vogais por "aê" (tipo um sotaque de brincadeira). Exemplo:

frase = input("Digite uma frase: ")

for letra in frase:
    if letra.lower() in "aeiou":
        print("aê", end="")
    else:
        print(letra, end="")

    