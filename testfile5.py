angka1 = float(input("Masukkan angka 1 = "))
operator = input("Operator (+,-,*,/) = ")
angka2 = float(input("Masukkan angka 2 = "))

if operator == "+":
  hasil = angka1 + angka2
  print(f"hasilnya adalah {hasil}")
  
if operator == "-":
  hasil = angka1 - angka2
  print(f"hasilnya adalah {hasil}")
  
if operator == "*":
  hasil = angka1 * angka2
  print(f"hasilnya adalah {hasil}")

if operator == "/":
  hasil = angka1 / angka2
  print(f"hasilnya adalah {hasil}")