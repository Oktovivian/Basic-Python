print("======= membuat list =======")
my_list1 = [] # list kosong

my_list2 = [1, 2, 3, 3] # list berisi integer

my_list3 = [True, 2, 'Tiga'] # list berisi nilai dengan berbeda type

my_list4 = [[90, 90], [100, 90]] # list berisi list lain

my_list5 = list([1, 2, 3])


print(my_list1)
print(my_list2)
print(my_list3)
print(my_list4)
print(my_list5)


print()
print("======= Mengakses elemen list =======")
print()

print(my_list2[2]) # mengakses elemen ke-3, yaitu integer 3
print(my_list3[0]) # mengakses elemen ke-1, yaitu boolean True
print(my_list4[0]) # mengakses elemen ke-1, yaitu list berisi [90, 90]
print(my_list4[1][0]) # mengakses elemen ke-1 dari elemen ke-2 my_list ([100, 90]),
#yaitu integer 100

print()
print("======= Iterasi elemen list =======")
print()
my_list = [5, 'empat', 3, (2, 1)]

for i in my_list: # mengakses seluruh elemen list satu per satu
    print(i)

sum_int = 0
for x in my_list: # mengakses seluruh elemen list satu per satu
    if isinstance(x, int):
        sum_int += x
print('Jumlah integer:',sum_int)


print()
print("======= Menambah elemen list =======")
print()

my_list = [1,'dua',3]
my_list.append('empat')
print(my_list)

my_list.extend([5, 6, 7])
print(my_list)

my_list.extend('halo') # 'halo' adalah iterable, sehingga setiap hurufnya menjadi satu buah elemen
print(my_list)

my_list.insert(1, 100) # menambahkan 100 di index ke-1 (posisi ke-2 di list), dan menggeser elemen setelahnya 1 posisi
print(my_list)


print()
print("======= Mengubah elemen list =======")
print()

my_list = [90,80,95,85,85,100,88,98,79,80]
my_list[0] = 10 # update 1 buah nilai
my_list[3:5] = [10, 10] # update beberapa nilai sekaligus dengan slicing
print(my_list)


print()
print("======= Menghapus elemen list =======")
print()
my_list = [90,80,95,85,85,100,88,98,79,80]

my_list.remove(80) # menghapus elemen 80 yang pertama kali ditemukan
print(my_list)
my_list.pop(4) # menghapus elemen ke-4 yaitu 100
print(my_list)
my_list.pop() # menghapus elemen terakhir yaitu 80
print(my_list)
nilai = my_list.pop(1) # pop akan mereturn nilai yang dikeluarkan dari list, sehingga bisa disimpan di sebuah variable untuk diproses lebih lanjut
print(nilai, my_list)
my_list.clear() # hapus semua elemen list
print(my_list)
