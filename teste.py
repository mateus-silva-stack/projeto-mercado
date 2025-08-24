banco_de_alimentos = {
    "Arroz": { "preço" : 19.90 , "data_validade" :  "28/01/2025" },
    "Feijao" : { "preço" : 11.99 , "data_validade" : "23/03/2025" },
    "Açucar" : { "preço" : 8.99 , "data_validade" : "26/06/2025" },
    "Macarrao" : { "preço" : 13.99 , "data_validade" : "12/06/2025" },
    "oleo" : { "preço" : 14.99 , "data_validade" : "30/06/2025" },
}
while True:
    produto = input("digite qual o produto você deseja: ").lower()

    if produto == "sair":
        print("Encerrando sistema...")
        break
    elif produto in banco_de_alimentos:
        print(banco_de_alimentos[produto])

    else:
        print("Produto não encontrado!")
  