nome = "vini"
idade = 18
profissao = "desempregado"
linguagem = "python"

print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho {1} e estou matriculado no curso de {0}".format(linguagem, profissao, idade, nome))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

#trabalho com dicionário

dados = {"nome1": "vini1", "idade1": "19", "profissao1": "duplamente desenpregado", "linguagem1": "php"}
print("Olá, me chamo {nome1}. Eu tenho {idade1} anos de idade, trabalho com {profissao1} e estou matriculado no curso de {linguagem1}".format(**dados))

#F string

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}")

#Formartar com f string

PI = 3.14159

print(f"O valor de PI: {PI:.2f}")

print(f"O valor de PI: {PI:10.2f}")