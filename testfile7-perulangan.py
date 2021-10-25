#a = [1, 2, 3]       # terbentuk sebuah list dengan 3 item
#print(a)
#print(type(a))      # terlihat bahwa type data a adalah list

#print()

#b = range(3)        # akan terbentuk range dengan 3 item yaitu 0, 1, 2
#print(b)            # menampilkan objek range
#print(list(b))      # untuk menampilkan isi, kita perlu ubah menjadi type list

#print

#c = range(10, 0, -1)
#print(list(c))

a = [3, 2, 1]
for i in a:
    print(i)

print("=================")

# buat list nama-nama hari
list_hari = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']

# print nama hari satu per satu
for hari in list_hari:
    print(hari)

print("=================")

# buat list nilai
list_nilai = [100, 20, 45, 80, 90, 30]

# hitung banyak nilai di bawah 50
u_50 = 0
for nilai in list_nilai:
    if nilai < 50:
        u_50 += 1

print(u_50)

print("=================")

for i in range(10):
    print(i, "Cinta Telkom University")

print("=================")

bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
# Cetak bulan ganjil saja
for i in range(0, len(bulan), 2):
    print(bulan[i])

