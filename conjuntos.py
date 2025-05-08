#Conjunto (set) é uma coleção de que não possui objetos repetidos. Usamos para representar conjuntos matemáticos ou eliminar itens duplicados
print(set([1,2,3,1,3,4]))

print(set("abacaxi"))

print(set(("palio", "gol", "celta", "palio")))

#Não é possível pegar valores específicos de um set. É necessário transforma-lo em lista para poder fazer isso
#Sets podem ser em chaves tbm
numeros = {1,2,3,4}
print(numeros)
numeros = list(numeros)
print(numeros[0])

#A forma mais comum para percorrer os dados de um conjunto é utilizando o comancdo for
carros = {"gol","monza","celta"}

for carro in carros:
    print(carro)
    
#enumerate
for indice,carro in enumerate(carros):
    print(f"{indice}: {carro}")
    
#---------CONJUNTOS COM SET------------
#{}union
conjunto_a = {1,2,3,4}
conjunto_b = {3,4,5,6}

print(conjunto_a)
print(conjunto_b)
print(conjunto_a.union(conjunto_b))

#{}intersection
print(conjunto_a.intersection(conjunto_b))

#{}diference
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

#{}symetric_difference
print(conjunto_a.symmetric_difference(conjunto_b))

#issubset
conjunto_c = {1,2,3}
conjunto_d = {4,1,2,5,6,3}

print(conjunto_c.issubset(conjunto_d))
print(conjunto_d.issubset(conjunto_c))

#issuperset
print(conjunto_c.issuperset(conjunto_d))
print(conjunto_d.issuperset(conjunto_c))

#isdisjoint
conjunto_1 = {1,2,3,4,5}
conjunto_2 = {6,7,8,9}
conjunto_3 = {1,0}

print(conjunto_1.isdisjoint(conjunto_2))
print(conjunto_1.isdisjoint(conjunto_3))

#add
sorteio = {1,23}

sorteio.add(25) #{1,23,25}
sorteio.add(42) #{1,23,25,42}
sorteio.add(25) #{1,23,25,42}

#clear
sorteio #{1,23,25,42}
sorteio.clear()
sorteio # {}

#copy
sorteio #{1,23,25,42}
sorteio.copy()
sorteio #{1,23,25,42}

#discard
#obs: remove é a msm coisa, unica difereça é q se usar o remove e um valor q não existe ele dá erro. Já o discard nn dá erro
numeros2 = {1,2,3,4,5,6,7,8,9,0}

numeros2.discard(1) #{2,3,4,5,6,7,8,9,0}
numeros2.discard(45) #{2,3,4,5,6,7,8,9,0}

numeros2 #{2,3,4,5,6,7,8,9,0}

#pop
numeros3 = {1,2,3,4,5,6,7,8,9,0}

numeros3 #{0,1,2,3,4,5,6,7,8,9,0}

numeros3.pop() #{0}
numeros3.pop() #{1}

numeros3 #{2,3,4,5,6,7,8,9,0}

#in
#verificar se tem algum numero

numeros2 #{2,3,4,5,6,7,8,9,0}

print(1 in numeros2)
print(2 in numeros2)