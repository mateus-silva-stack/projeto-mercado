import json

banco = {
    "Arroz": { "preço" : 19.90 , "data_validade" :  "28/01/2025" },
    "Feijao" : { "preço" : 11.99 , "data_validade" : "23/03/2025" },
    "Açucar" : { "preço" : 8.99 , "data_validade" : "26/06/2025" },
    "Macarrao" : { "preço" : 13.99 , "data_validade" : "12/06/2025" },
    "oleo" : { "preço" : 14.99 , "data_validade" : "30/06/2025" },
}

with open ("banco.json","w") as arquivo:
    json.dump(banco, arquivo, indent=4 )

with open("banco.json", "r") as arquivo:
    dados = json.load(arquivo)
while True: 
    produto = input("qual produto você deseja consultar? ")

    if produto in dados:
        print(dados[produto])
        
    else:
       print("Produto não encontrado")