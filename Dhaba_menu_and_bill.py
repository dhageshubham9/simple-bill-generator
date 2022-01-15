#WAP  to give menu and print bill

print("-------------------------------------------------------")
print("                Welocome to Resotonant                  ")
print("-------------------------------------------------------")
print("\n                  Menu Card                   ")
print("\n\nOur Dishes: ")
print("\nPizza:")
print("\n Small Pizza = 150/-")
print("\n Medium Pizza = 200/-")
print("\n Large Pizza = 250/-")
print("\n Peporoni for Small Pizza = 20/-")
print("\n Peporoni for Large & Medium Pizza = 30/-")
print("\n Extra Cheese for Any Size = 10/-")
Pizza=0
Peporoni=0
Cheese=0
Size=str(input("Please Enter your pizza size S , M OR L: "))
Pepo=str(input("Please tell peporoni provide or not (Y=YES/N=NO): "))
Chez=str(input("Please tell Cheese provide or not (Y=YES/N=NO): "))
if(Size=="S" ):
    Pizza=150
    if(Pepo=="Y"):
        Peporoni=20
    if(Chez=="Y"):
        Cheese=10
elif(Size=="M"):
    Pizza=200
    if(Pepo=="Y"):
        Peporoni=30
    if(Chez=="Y"):
        Cheese=10
elif(Size=="L"):
    Pizza=250
    if(Pepo=="Y"):
        Peporoni=30
    if(Chez=="Y"):
        Cheese=10
#calculate all values
Total=Pizza + Peporoni + Cheese
print("Your Total Bill is :" , Total)
print("-------------------------------------------------------")
print("\n                    Thank You!                     \n")
print("-------------------------------------------------------")


