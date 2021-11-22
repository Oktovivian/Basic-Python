print("Membuat Set")
my_set1 = {1, 4, 'telU', 4} # membuat set dengan kurung kurawal, set hanya akan menyimpan 1 buah nilai 4
print(my_set1)
my_set2 = set([1, 'telu', 4, 'telu']) # membuat set dengan set()
print(my_set2)
my_set3 = {} # jika set awal kosong, maka membuat set hanya bisa dengan set(). Karena {} digunakan untuk membuat dictionary
print(type(my_set3))
my_set4 = set()
print(type(my_set4))



print()
print("===== Mengakses elemen set =====")
print()

my_set = {1, 2, 3}
print(5 in my_set)

for i in my_set: # perlu diingat set tidak terurut, sehingga urutannya bisa berubah dan tidak konsisten
    print(i)



print()
print("===== Menambah elemen set =====")
my_set = {1, 2, 3}
my_set.add(5)
print(my_set)
my_set.update([6, 7, 8])
print(my_set)
try:
    my_set.add([9, 10])
except Exception as e:
    print('Error:', e)
my_set.add(tuple([9, 10]))
print(my_set)




print()
print("Set adalah mutable, namin elemen pada set tidak dapatet tidak bisa diubah atau diganti setelah ditambahkan ke dalam set.")
print()




print()
print("===== Menghapus elemen set =====")
print()

my_set = {1, 2, 3, 4}

my_set.remove(1)
print(my_set)

try:
    my_set.remove(5) # menimbulkan exception karena 5 tidak ada dalam set.
except Exception as e:
    print('Error:', e)

my_set.discard(4)
print(my_set)
    
my_set.discard(5) # tidak menimbulkan exception meskipun 5 tidak ada dalam set.
print(my_set)

p = my_set.pop()
print('pop1:', p, my_set)
q = my_set.pop()
print('pop2:', q, my_set)
r = my_set.pop() # menimbulkan exception karena set kosong, tidak ada nilai yang bisa di-pop
print('pop3:', r, my_set)
