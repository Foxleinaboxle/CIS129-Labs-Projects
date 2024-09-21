#Vixen Hinkle
#9/20/24
#cis 129 mod 3 lab "Coffe shop"

#display "Welcome to coffe shop, we have Coffee and Cake"
print("Welcome to coffe shop, we have Coffee, Cake, Eggs Benedict, and Tea. ")
#Ask Input (Coffee) "how much coffee would you like? "
Coffee = int(input("How much coffee would you like? "))
#Ask Input (Cake) "how much Cake would you like? "
Cake = int(input("how much Cake would you like? "))
#Ask Input (Eggy) "how much Eggs Benedict would you like? "
Eggy = int(input("how much Eggs Benedict would you like? "))
#Ask Input (Tea) "how much Tea would you like? "
Tea = int(input("how much Tea would you like? "))
#Combine inputs into price
Coffee_Price = int(Coffee + 5)
Cake_Price = int(Cake + 3)
Eggy_Price = int(Eggy + 6)
Tea_Price = int(Tea + 4)
Order_Total = Coffee_Price + Cake_Price + Eggy_Price + Tea_Price
#Display Resepte "Thank you for ordering here is your recipt"
print("Thank you for ordering here is your Recipt. ")
print("==============================================")
print("Coffee ", "Amount",Coffee, " ", "Cost $",Coffee_Price)
print("Cake ", "Amount",Cake, " ", "Cost $",Cake_Price)
print("Eggs Benedict ", "Amount",Eggy, " ", "Cost $",Eggy_Price)
print("Tea ", "Amount",Tea, " ", "Cost $",Tea_Price)
print("Total $",Order_Total)
print("==============================================")
