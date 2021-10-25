x = 1
jlh_genap = 0
jlh_ganjil = 0
while x <= 5:
    if x % 2 == 0:
        jlh_genap = jlh_genap + x
    else:
        jlh_ganjil = jlh_ganjil +x
    x = x + 1

print("Jumlah bilangan genap dari 1-5 adalah :", jlh_genap)
print("Jumlah bilangan ganjil dari 1-5 adalah :", jlh_ganjil)