#Lista é um objeto e uma estrutura de dados que consegue armazenar outros objetos
#Se a lista é um objeto ela consegue aramazenar outras listas e quando isso ocorre se dá o nome de: LISTA ANINHADA!
#Listas aninhadas podemos representar matrizes, estruturas bidimensionais (tabelas)

frutas = ["banana","maça","pera","uva"]
print(frutas)

print(frutas[0])
print(frutas[1])
print(frutas[-1])
print(frutas[-2])
#Pode-se declarar uma lista vazia
frutas = []

letras = list("Python")
print(letras)

numeros = list(range(10))
print(numeros)
carro1 = ["Ferrari","F8",4200000, 2020, 2900, "São Paulo", True]
print(carro1)

#Iterar Listas
carros = ["Gol","Celta","Palio"]
for carros in carros:
    print(carros)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#COMPRESSÃO DE LISTAS
#Primeira versão
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numeros in numeros:
    if numeros % 2 == 0:
        pares.append(numeros)
        

#Modificando a primeira versão
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numeros in numeros:
    quadrado.append(numeros ** 2)


#Segunda versão
numeros2 = [2, 31, 22, 3, 5, 55, 37]
pares = [numeros2 for numeros2 in numeros2 if numeros2 % 2 == 0]
print(f"{pares}")
#Modificando a segunda versão

numeros2 = [2, 31, 22, 3, 5, 55, 37]
quadrado = [numeros2 **2 for numeros2 in numeros2 ]
print(quadrado)

#MATRIZ
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

# Acessos à matriz
print("Matriz completa:", matriz)
print("Primeira linha:", matriz[0])
print("Primeiro elemento da primeira linha:", matriz[0][0])
print("Último elemento da primeira linha:", matriz[0][-1])
print("Último elemento da última linha:", matriz[-1][-1])


