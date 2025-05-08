def exibir_mensagem():
    print("Olá Mundo")

def exibir_mensagem_2(nome):
    print(f"Olá Mundo {nome}!")
    
def exibir_mensagem_3(nome="Vini"):
    print(f"Olá Mundo {nome}")
    
exibir_mensagem()
exibir_mensagem_2(nome="Vinicius")
exibir_mensagem_3()
exibir_mensagem_3(nome = "Fudido games")


#return
def calcular_total(numeros):
    return sum(numeros)
def retorna_antecessor_sucessor(numeros):
    antecessor = numeros - 1
    sucessor = + 1

    return antecessor, sucessor

print(calcular_total([10, 9, 8, 7, 6, 5, 4, 3 ,2 ,1]))

print(retorna_antecessor_sucessor(10))

# argumentos nomeados
# usando argumentos nomeados da fomra chave=valor
def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {placa}/{modelo}/{ano}/{placa}")
    
salvar_carro("Fiat","Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca":"Fiat","modelo":"Palio","ano":1999,"placa":"ABC-1234"})




  