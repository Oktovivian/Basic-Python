print("Menu Hari Ini",'\n',1,'=','Nasi Goreng','\n',2,'Nasi Uduk','\n',3,'Nasi Remes')
print("Topping Hari ini",'\n',1,'=','Mozarella','\n',2,'=','Sosis',3,'=','Bihun')

print("================")

print("Nasi_Goreng = 10000")
print("Nasi_Uduk = 12000")
print("Nasi_Remes = 15000")

print("================")

print("Mozarella = 10000")
print("Sosis = 5000")
print("Bihun = 6000")

print("================")

Nasi_Goreng = 10000
Nasi_Uduk = 12000
Nasi_Remes = 15000

Mozarella = 10000
Sosis = 5000
Bihun = 6000

pilih_menu_makan = int(input("Pilih menu makanmu = "))
pilih_topping_makan = int(input("Pilih topping makanmu = "))

if pilih_menu_makan == 1:
    if pilih_topping_makan == 1:
        print("makanmu1 adalah nasi goreng dengan mozarella dengan harga",'=',Nasi_Goreng + Mozarella)
    elif pilih_topping_makan == 2:
        print("makanmu adalah nasi goreng dengan sosis dengan harga",'=',Nasi_Goreng + Sosis)
    elif pilih_topping_makan == 3:
        print("Makanmu adalah nasi goreng dengan bihun dengan harga",'=',Nasi_Goreng + Bihun)
    else:
        print("makanmu adalah nasi goreng dengan harga",'=',Nasi_Goreng)
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