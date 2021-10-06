print("pilih menu makanan dengan menekan",'=',1,2,3)
print("pilih topping makanan dengan menekan",'=','\n',1,'=','lettuce','\n',2,'=','tommato','\n',3,'=','keju')

pilih_menu_makan = int(input("Pilih menu makanmu = "))
pilih_topping_makan = int(input("Pilih topping makanmu = "))
if pilih_menu_makan == 1:
    if pilih_topping_makan == 1:
        print("makanmu1 adalah nasi goreng dengan lettuce")
    elif pilih_topping_makan == 2:
        print("makanmu adalah nasi goreng dengan tomat")
    else:
        print("makanmu adalah nasi goreng dengan keju")
elif pilih_menu_makan == 2:
    if pilih_topping_makan == 1:
        print("makanmu adalah mie goreng dengan lettuce")
    elif pilih_topping_makan == 2:
        print("makanmu adalah mie goreng dengan tomat")
    else:
        print("makanmu adalah mie goreng dengan keju")
elif pilih_menu_makan == 3:
    if pilih_topping_makan == 1:
        print("makanmu adalah mie rebus dengan lettuce")
    elif pilih_topping_makan == 2:
        print("makanmu adalah mie rebus dengan tomat")
    else:
        print("makanmu adalah mie rebus dengan keju")
else:
    print("ojo kemaruk, cok")