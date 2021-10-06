print("Selamat Datang di Resto Bento")

print("================")

print("Menu Hari Ini",'\n',1,'=','Nasi Goreng','\n',2,'=','Nasi Uduk','\n',3,'=','Nasi Remes')
print("Topping Hari ini",'\n',1,'=','Mozarella','\n',2,'=','Sosis','\n',3,'=','Bihun')

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

masukkan_menu = int(input("Pilih menu anda = "))
masukkan_topping = int(input("Pilih topping anda = "))

if masukkan_menu == 1:
    if masukkan_topping == 1:
        print("Nasi Goreng dengan Mozarella dengan harga",'=',Nasi_Goreng + Mozarella)
    elif masukkan_topping == 2:
        print("Nasi Goreng dengan Sosis dengan harga",'=',Nasi_Goreng + Sosis)
    elif masukkan_topping == 3:
        print("Nasi Goreng dengan Bihun dengan harga",'=',Nasi_Goreng + Bihun)
    else:
        print("Nasi Goreng dengan harga",'=',Nasi_Goreng)
elif masukkan_menu == 2:
    if masukkan_topping == 1:
        print("Nasi Uduk dengan Mozarella dengan harga",'=',Nasi_Uduk + Mozarella)
    elif masukkan_topping == 2:
        print("Nasi Uduk dengan Sosis dengan harga",'=',Nasi_Uduk + Sosis)
    elif masukkan_topping == 3:
        print("Nasi Uduk dengan Bihun dengan harga",'=',Nasi_Uduk + Bihun)
    else:
        print("Nasi Uduk dengan harga",'=',Nasi_Uduk)
elif masukkan_menu == 3:
    if masukkan_topping == 1:
        print("Nasi Remes dengan Mozarella dengan harga",'=',Nasi_Remes + Mozarella)
    elif masukkan_topping == 2:
        print("Nasi Remes dengan Sosis dengan harga",'=',Nasi_Remes + Sosis)
    elif masukkan_topping == 3:
        print("Nasi Remes dengan Bihun dengan harga",'=',Nasi_Remes + Bihun)
    else:
        print("Nasi Remes dengan harga",'=',Nasi_Remes)
else:
    print("Menu Tidak Tersedia")

print("Terima Kasih sudah makan di restoran kami")