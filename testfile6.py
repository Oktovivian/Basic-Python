nilai = [7, 2, 4, 9, 1, 6, 0, 5]

print("Sebelum diurutkan:", nilai)

for i in range(len(nilai)-1):
    idx_min = i
    # cari posisi nilai minimum pada range index ke-i sampai akhir
    for j in range(i+1, len(nilai)):
        # jika nilai ke-j lebih kecil dari nilai min saat ini (yg ditunjuk idx_min)
        # simpan posisi j sebagai idx_min yang baru
        if nilai[j] < nilai[idx_min]:
            idx_min = j
    # tukar posisi nilai minimum ke posisi ke-i
    temp = nilai[idx_min]
    nilai[idx_min] = nilai[i]
    nilai[i] = temp

    # tukar posisi pada python bisa juga dengan cara berikut:
    # nilai[i], nilai[idx_min] = nilai[idx_min], nilai[i]

print("Setelah diurutkan:", nilai)