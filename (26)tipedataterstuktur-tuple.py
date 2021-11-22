print("Membuat Tuple")

my_tuple = tuple() # bisa dengan tuple()
print(my_tuple)
my_tuple1 = ("Jono", 24, 175, 60) # atau cukup dengan buka dan tutup kurung
print(type(my_tuple1))
my_tuple2 = "Jene", 25, 165, 50
print(type(my_tuple2))

# khusus jika tuple hanya berisi 1 item, maka perlu ditambahkan 1 buah koma stelahnya
my_tuple3 = (1,)
print(type(my_tuple3))
my_tuple4 = 1,
print(type(my_tuple4))
# jika tanpa koma maka tidak menjadi tuple
my_tuple5 = (1)
print(type(my_tuple5))

# seperti list, bisa berisi type data berbeda, termasuk tuple dan list
my_tuple6 = (1, 2, 1, (4, 5), [1, 2])
print(my_tuple6)



print()
print("===== Mengakses elemen tuple =====")
print()

my_tuple6 = (1, 2, 1, (4, 5), [1, 2])

print(my_tuple6[1])
print(my_tuple6[-1])
print(my_tuple6[3][1])
print(my_tuple6[1:4])
print(my_tuple6.index(2))
print((4, 5) in my_tuple6)



print()
print("===== Menambah, mengubah, menghapus elemen tuple =====")
print()

my_tuple = ("immutable", ["mutable1", "mutable2"]) # tuple immutable, namun elemen kedua tersebut adalah sebuah list yang mutable
try:
    my_tuple[1] = ["test", "test"] #akan menimbulkan error
except Exception as e:
    print('Error:', e)
my_tuple[1][0] = "mutable3" # tidak error
print(my_tuple)
my_tuple[1].append("mutable4") # juga diperbolehkan karena mengubah mutable object
print(my_tuple)
