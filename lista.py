
#lista de compras utilizando o for
groceries= []
while True:

  question= int(input("How many products would you like to buy?"))
  for i in range(question):
     product= input("Which product would you like to buy?")
     groceries.append(product) #adicionar a lista

  print("These are your products:")
  for product in groceries:
     print(product)
 
 #adicionar mais itens
  question2= input("Would you like to buy anything else?").strip().lower()
  if question2 != "yes":
     print("Thank you for shopping at our market! These are your products:")
     break









