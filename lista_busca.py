

#lista de programas

funcionarios = ["Ana", "Carlos", "Beatriz", "João", "Mariana", "Pedro"]


nome = input("Digite o nome do funcionário que deseja buscar: ")

for funcionario in funcionarios:
      if funcionario == nome:
        print("Funcionário encontrado:", funcionario)
        break

print ("Fim da busca.")

