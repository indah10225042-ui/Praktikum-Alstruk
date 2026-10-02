# Program untuk menentukan apakah input angka genap atau ganjil

# Mengambil input angka (bilangan bulat) dari pengguna
angka = int(input("Masukkan angka: "))

# Mengecek apakah angka habis dibagi 2
if angka % 2 == 0:
    print("genap")
else:
    print("ganjil")