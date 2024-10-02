#calculadora imc
pergunta= input("Olá! Bem-vindo a calculadora de IMC! Vamos calcular seu índice de massa corporal? (responda com sim ou não)").strip().lower()
while True:
  if pergunta != "sim":
     print("Sem problemas! Lembre-se, sempre que precisar a calculadora IMC estará a sua disposição. Até Breve!")
     break
  else: #pergunta == sim
     peso= float(input("Digite o seu peso (Kg):"))
     altura= float(input("Agora, digite sua altura (metros):"))
     IMC= peso/altura**2
     imc= round(IMC,2)
     print("Seu IMC é:", imc)
     # apresentando classificação do IMC
     if imc < 17:
         print("E é classificado como muito abaixo do peso")
     elif 17<= imc <=18.49:
         print("E é classificado como abaixo do peso")
     elif 18.5<= imc <=24.99:
         print("E é classificado como peso normal")
     elif 25<= imc <=29.99: 
         print("E é classificado como acima do peso") 
     elif 30<= imc <=34.99:
         print("E é classificado como obesidade")
     elif 35<= imc <=39.99:
         print("E é classificado como obesidade severa")
     else: # imc < 40
         print("E é classificado como obesidade mórbida")
        
     # pergunta se o usuário deseja continuar
     resposta= input("Deseja calucar outro IMC? (responda com sim ou não)").strip().lower()
     if resposta != "sim":
          print("Então meu trabalho termina por aqui! Espero que a calculado de IMC tenha te ajudado =)")
          break
     else: 
         print("Então vamos calcular novamente!")
    
  