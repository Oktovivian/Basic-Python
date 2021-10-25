def hitung_luas_lingkaran(r):
    luas =  3.14 * r**2
    return luas
    
luas = hitung_luas_lingkaran(10)
print(luas)

print(hitung_luas_lingkaran(10) + hitung_luas_lingkaran(20))

print()
# fungsi menampilkan menu makanan
def tampil_menu():
    print('Menu 1: Udang Bakar')
    print('Menu 2: Ayam Goreng')
    print('Menu 3: Cumi Rebus')

x = tampil_menu()
print("Nilai fungsi :", x)

print()
# fungsi untuk menghitung luas lingkaran
def hitung_luas_lingkaran(r):
    luas =  3.14 * r**2
    return luas
    
def hitung_volume_tabung(r, t):
    return hitung_luas_lingkaran(r) * t
    
print(hitung_volume_tabung(10, 10))

print()
# fungsi untuk memprint dengan tambahan dekorasi tertentu
def my_print(jlh, kata):
    """
    Fungsi untuk memprint kata dengan jumlah tertentu.

    Parameters:
    jlh (integer) : kata akan di print sebanyak jlh kali
    kata (string) : kata yang akan diprintkan
    """
    print("Kita akan print sebanyak", jlh, "kali")
    print("-"*30)
    """
    ini bukan docstring
    namun tetap tidak dianggap sebagai kode yang harus dieksekusi
    """
    for i in range(jlh):
        print("Cinta", kata)
    print("-"*30)