print("Membuat Dictionary")
my_dict1 = {}
print(type(my_dict1))
my_dict2 = dict()
print(type(my_dict2))

my_dict3 = {1: 'satu', 2: 'dua', (3, 4): [1, 2, 3], 'four': {1: 'senin', 2: 'selasa'}}

my_dict4 = dict([(1, 'satu'), (2, 'dua'), ((3, 4), [1, 2, 3]), ('four', {1: 'senin', 2: 'selasa'})])

print(my_dict3)
print(my_dict4)

#my_dict5 = {[1, 2]: 'satu'} #error karena key tidak boleh mutable





print()
print("===== Mengakses elemen dictionary =====")
print()

my_dict = {1: 'satu', 2: 'dua', (3, 4): [1, 2, 3], 'four': {1: 'senin', 2: 'selasa'}}

print(my_dict[1])
print(my_dict[(3, 4)])
print(my_dict['four'])
print(my_dict['four'][2])

print(my_dict.get(10))

#print(my_dict[10]) #akan menimbulkan exception KeyError





print()
print("===== Cek keanggotaan dictionary (<key> in <my_dict>)======")
print()

my_dict = {1: 'satu', 2: 'dua', (3, 4): [1, 2, 3], 'four': {1: 'senin', 2: 'selasa'}}

print(1 in my_dict)
print(10 in my_dict)




print()
print("===== Iterasi elemen dictionary =====")
print()

my_dict = {1: 'satu', 2: 'dua', (3, 4): [1, 2, 3], 'four': {1: 'senin', 2: 'selasa'}}

for k in my_dict:
    print(k)

for k, v in my_dict.items():
    print('key:', k,' val:', v)






print()
print("===== Menambah elemen dan mengganti value =====")
print()

my_dict = {1: 'satu', 2: 'dua', (3, 4): [1, 2, 3], 'four': {1: 'senin', 2: 'selasa'}}

my_dict[10] = 'sepuluh' #key 10 belum ada, sehingga ditambahkan pasangan key-value ke dalam dictionary
print(my_dict)

my_dict[10] = 'ten' #key 10 sudah ada, sehingga value diupdate
print(my_dict)



print()
print("===== Menghapus elemen dictionary =====")
print()

my_dict = {1: 'satu', 2: 'dua', (3, 4): [1, 2, 3], 'four': {1: 'senin', 2: 'selasa'}}

v = my_dict.pop(1) #pop mengembalikan value dari key yang di-pop
print(v)
print(my_dict)

kv = my_dict.popitem() #popitem mengembalikan sembarang tuple (key, value)
print(kv)

my_dict.clear()
print(my_dict)

