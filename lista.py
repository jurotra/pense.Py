
#lista de compras utilizando o for
lista= []
while True:

  pergunta= int(input("Vamos as compras! Quantos itens voce gostaria de comprar?"))
  for i in range(pergunta):
     item= input("Qual item voce gostaria de colocar?")
     lista.append(item) #adicionar a lista

  print("Esses são seus itens:")
  for item in lista:
     print(item)
 
 #adicionar mais itens
  pergunta2= input("Gostaria de adicionar mais algum item?").strip().lower()
  if pergunta2 != "sim":
     print("Obrigada por comprar em nosso estabelecimento! Essa é a sua sacola de compras final:")
     break
  else:
     pergunta3= int(input("Quantos itens voce gostaria de adicionar?"))
     for i in range(pergunta3):
       item= input("Qual item voce gostaria de colocar?")
       lista.append(item) 
     print("Obrigada por comprar em nosso estabelecimento! Essa é a sua sacola de compras final:")
     for item in lista:
           print(item)
     break






