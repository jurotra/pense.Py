lado = 20
altura= 5

for i in range(lado):
    if i==0: 
        print("_"*lado)
    elif i==5:
        print(" "*8+"_"*5+" "*7)
for j in range(altura):
     print("|"+" "*(lado-2)+"|")
for i in range(lado):
    if i==lado-1:
        print("_"*lado)

  

 


 
