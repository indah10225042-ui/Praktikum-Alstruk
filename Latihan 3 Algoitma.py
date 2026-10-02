# Program untuk menentukan apakah suatu bilangan adalah bilangan prima atau bukan

# Mengambil input angka dari pengguna
angka = int(input("Masukkan angka: "))

# Bilangan prima harus lebih besar dari 1
if angka > 1:
    is_prima = True
    # Pengecekan pembagi dari 2 hingga angka - 1
    for i in range(2, angka):
        if angka % i == 0:
            is_prima = False
            break  # Jika ditemukan pembagi, bukan bilangan prima
            
    if is_prima:
        print(f"{angka} adalah bilangan prima")
    else:
        print(f"{angka} bukan bilangan prima")
else:
    print(f"{angka} bukan bilangan prima")