lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)

#[].clear
lista1 = [2, "Python2", [50, 40, 30]]

print(lista1)

lista1.clear()

print(lista1)

#copy serve pra copiar a lista origina
lista2 = [3, "Python3", [60, 50, 40]]

lista2.copy()

print(lista2)

#Count quantas vezes algo se repete
cores = ["vermelho","laranja","azul","ciano","vermelho"]

print(cores.count("vermelho"))
print(cores.count("laranja"))
print(cores.count("azul"))
print(cores.count("ciano"))

#Extend
linguagens = ["python", "js", "c"]

print(linguagens)

linguagens.extend(["java", "csharp"])

print(linguagens)

#Index
linguagens = ["python", "java", "c", "ruby"]

print(linguagens.index("java"))
print(linguagens.index("ruby"))

#Pop(semore tira o ultimo elemento)
linguagens1 = ["python", "js", "c", "java", "csharp"]

print(linguagens1.pop())
print(linguagens1.pop())
print(linguagens1.pop())
print(linguagens1.pop(0))

#remove
linguagens1 = ["python", "js", "c", "java", "csharp"]

linguagens1.remove("c")

print(linguagens1)

#reverse
linguagens1 = ["python", "js", "c", "java", "csharp"]

linguagens1.reverse()

print(linguagens1)

#sort é em ordem alfabética(nao da pra imprimir)
linguagensq = ["python1", "js", "c", "java", "csharp"]
linguagensq.sort()
print(f"A{linguagensq}")

linguagensw = ["python1", "js", "c", "java", "csharp"]
linguagensw.sort(reverse=True)
print(linguagensw)

linguagense = ["python1", "js", "c", "java", "csharp"]
linguagense.sort(key=lambda x: len(x))
print(linguagense)

linguagensr = ["python1", "js", "c", "java", "csharp"]
linguagensr.sort(key=lambda x: len(x), reverse=True)
print(linguagensr)

#len(lista quantos itens no na list)
inguagens1 = ["python", "js", "c", "java", "csharp"]
print(len(linguagens1))

#sorted(msm coisa do sort porem ele é uma função)
inguagens1 = ["python", "js", "c", "java", "csharp"]
sorted(linguagens1, key=lambda x:len(x))
print(linguagens1)

sorted(linguagens1, key=lambda x:len(x), reverse=True)
print(linguagens1)