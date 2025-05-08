#É um conjunto não ordenado de pares chave: valor, onde as chaves são únicas em dada instância do dicionário.
#dicionários são delimitados por chaves {} e é separado por vírgulas

pessoa = {"nome": "Vini","idade": 18}

#é a msm coisa de cima porem usa-se dict
pessoa = dict(nome="Vini", idade=18)

pessoa["telefone"] = "9933-2001"

print(pessoa)

print("-----------------")
#exemplo2
dados = {"nome": "VINI", "idade": 18, "telefone": "9999-9999"}

print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])

print(dados)

dados["nome"] = "Maria"
dados["idade"] = 20
dados["telefone"] = "1111-1111"

print(dados)

#MÉTODOS DICT
#{}clear
contatos ={
    "blablabla@yahoo.com" : {"nome": "Guilherme", "telefone": "6969-6969"} 
}
print(contatos)
contatos.clear()
print(contatos)
contatos ={
    "blablabla@yahoo.com" : {"nome": "Guilherme", "telefone": "6969-6969"} 
}

#{}copy.Quer alterar o dicionário mas sem mexer no dicionário principal
copia = contatos.copy()
copia["blablabla@yahoo.com"] = {"home": "don pollio"}

contatos["blablabla@yahoo.com"]
copia["blablabla@yahoo.com"]

print(copia)
print(contatos)

#fromkeys
dict.fromkeys(["nome","telefone"]) #{"nome": None, "teledone": None}

dict.fromkeys(["nome", "telefone"], "vazio") #{"nome": "vazio", "telefone": "vazio"}

#get{}
contatos1 = {
    "blublublu@gmail.com": {"nome": "Vini", "telefone":"9999-0000"}
}               

#contatos["chave"] #keyerror

contatos.get("chave")#None
contatos.get("chave",{})#{}
contatos.get("blublublu@gmail.com",{}) #{"blublublu@gmail.com": {"nome": "Vini", "telefone":"9999-0000"}}

#{}items
contatos1 = {
    "blublublu@gmail.com": {"nome": "Vini", "telefone":"9999-0000"}
}    

print(contatos1.items())

#{}keys
contatos1 = {
    "blublublu@gmail.com": {"nome": "Vini", "telefone":"9999-0000"}
}    

print(contatos1.keys())

#pop{}: remove e retornar o valor q ele removeu
contatos2 = {
    "blublublu@gmail.com": {"nome": "Vini", "telefone":"9999-0000"}
}

resultado = contatos2.pop("blublublu@gmail.com")
print(resultado)
resultado = contatos2.pop("blublublu@gmail.com", {})
print(resultado)    