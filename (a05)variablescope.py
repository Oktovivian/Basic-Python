# ini contoh pertama
x = 10

def cetak():
    print("dalam fungsi:", x)

cetak()


# ini contoh kedua
print()
#keyword global
x = 10

def tambah():
    global x # maka x yang dimaksud dalam fungsi ini adalah x global, meskipun ada x di-assign nilai baru
    y = x + 1
    x = y

tambah()
print("setelah fungsi:", x)
print()


# ini contoh ketiga
def foo():
    local_foo = 10
    def bar():
        print("variable local_foo dari dalam bar:", local_foo)
    
    bar()

foo()