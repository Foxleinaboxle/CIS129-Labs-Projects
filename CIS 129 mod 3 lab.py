#Vixen Hinkle
#9/20/24
#cis 129 mod 3 lab "Coffe shop"

#display "Welcome to coffe shop, we have Coffee and Cake"
print("Welcome to coffe shop, we have Coffee and Cake. ")
#Ask Input (Coffee) "how much coffee would you like? "
Coffee = int(input("How much coffee would you like? "))
#Ask Input (Cake) "hou much Cake would you like? "
Cake = int(input("how much Cake would you like? "))
#Combine inputs into price
Coffee_Price = int(Coffee + 5)
Cake_Price = int(Cake + 3)
Order_Total = Coffee_Price + Cake_Price
#Display Resepte "Thank you for ordering here is your recipt"
print("Thank you for ordering here is your Recipt. ")
print("==============================================")
print("Coffee ", "Amount",Coffee, " ", "Cost $",Coffee_Price)
print("Cake ", "Amount",Cake, " ", "Cost $",Cake_Price)
print("Total $",Order_Total)
print("==============================================")
