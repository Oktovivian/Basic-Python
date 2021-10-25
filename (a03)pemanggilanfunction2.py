# fungsi untuk memprint dengan tambahan dekorasi tertentu
print('contoh ketiga')
def my_print(jlh, kata):
    """
    Fungsi untuk memprint kata dengan jumlah tertentu.

    Parameters:
    jlh (integer) : kata akan di print sebanyak jlh kali
    kata (string) : kata yang akan diprintkan
    """
    print("Kita akan print sebanyak", jlh, "kali")
    print("-"*30)
    for i in range(jlh):
        print("Cinta", kata)
    print("-"*30)
    
my_print(10, "halo")
print()


# fungsi untuk menghitung luas lingkaran
print('contoh keempat')
def hitung_luas_lingkaran(r):
    luas =  3.14 * r**2
    return luas
    
def hitung_volume_tabung(r, t):
    return hitung_luas_lingkaran(r) * t
    
print(hitung_volume_tabung(10, 10))