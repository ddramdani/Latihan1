import os

def header():
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^50}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^50}")
    print(f"{'-'*50:^50}")
# input user
def input_user():
    panjang = int(input("Masukan Panjang = "))
    lebar = int(input("Masukan Lebar = "))
    return panjang,lebar
def hitung_luas(panjang,lebar):
    return panjang*lebar
def hitung_keliling(panjang,lebar):
    return 2*(panjang+lebar)
def display(message,value):
    print(f"Hasil Perhitungan {message} = {value}")
# looping
while True:
    header()
    opsi = input("Silahkan Masukan Pilihan Anda (1/2)\n 1. Menghitung Luas Persegi P \n 2. Mengitung Keliling Persegi P \n = ")
    if opsi == "1":
        lebar,panjang = input_user()
        luas =hitung_luas(panjang,lebar)
        display("Luas",luas)
    elif opsi == "2":
        lebar,panjang = input_user()
        keliling = hitung_keliling(panjang,lebar)
        display("Keliling",keliling)

    isCountinue = input("Apakah Lanjut (y/n) = ")
    if isCountinue == "n":
        break
print("Program Selesai, Terima Kasih")