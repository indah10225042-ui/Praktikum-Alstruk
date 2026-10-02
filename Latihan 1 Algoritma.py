# Program untuk menentukan apakah suatu bilangan Positif, Negatif, atau Nol

# Mengambil input angka dari pengguna
angka = float(input("Masukkan sebuah angka: "))

# Mengecek kondisi bilangan
if angka > 0:
    print(f"Angka {angka} adalah bilangan Positif")
elif angka < 0:
    print(f"Angka {angka} adalah bilangan Negatif")
else:
    print("Angka tersebut adalah Nol")