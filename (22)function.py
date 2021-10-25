# mendefinisikan fungsi
def fungsi():
    print("Ini adalah fungsi")
# memanggil fungsi
fungsi()

print()
# membuat fungsi sederhana
def suara_ayam():
    print('kukuruyuk')

def harga_ayam():
    suara_ayam()
    print('Harga ayam per 1kg adalah Rp20.000')

# membuat fungsi dengan input argumen
def hargatotalayam(kg):
    suara_ayam()
    harga = 20000
    hargaTotal = kg*harga
    print('harga',kg,'kg ayam adalah',hargaTotal)

harga_ayam()
hargatotalayam(2)
hargatotalayam(0.5)
hargatotalayam(9)
 

