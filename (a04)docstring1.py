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
    