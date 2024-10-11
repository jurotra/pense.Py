print("\n★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★")
print("This program prints a little house!")
print("★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★ ★\n\n")

height = int(input("Please enter the height of the house: "))
width = int(input("Please enter the width of the house: "))
print("\n")

roof = " "*2 + "/" + " " * (width-4) + "\\" + " "*2 + "\n" + " " + "/" + " " * (width-2) + "\\" + " " + "\n" + "/" + "-" * width + "\\" + "\n" 
wall = "|" + " " * width + "|" + "\n"
wall = wall * height
floor= "-"*(width+2)


house = roof + wall + floor
print(house)


  

 


 
