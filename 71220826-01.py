def tambah(bilangan1, bilangan2):
    return bilangan1 + bilangan2

def kurang(bilangan1, bilangan2):
    return bilangan1 - bilangan2

def bagi(bilangan1, bilangan2):
    return bilangan1 / bilangan2

def kali(bilangan1, bilangan2):
    return bilangan1 * bilangan2

while True:
    print("\n========== Kalkulator Sederhana ==========")
    print("Pilih Operasi")
    print("Tambah   (1)")
    print("Kurang   (2)")
    print("Kali     (3)")
    print("Bagi     (4)")
    print('Keluar   (Q)')
    operasi = input("Masukan Pilihan (1/2/3/4/Q):").lower()
    if operasi=='q':
        print('Terimakasih, sampai Jumpa!')
        break
    bilangan1 = eval(input("Masukan Angka Pertama :"))
    if bilangan1=='q' or bilangan1=="Q":
        print('Program Terhenti, sampai Jumpa!')
        break
    bilangan2 = eval(input("Masukan Angka Kedua :"))
    if bilangan2=='q' or bilangan2=="Q":
        print('Program Terhenti, sampai Jumpa!')
        break
    if isinstance(bilangan1,int) and isinstance(bilangan2,int):
        if operasi == '1':
            print(f"Hasil {bilangan1} + {bilangan2} =", tambah(bilangan1, bilangan2))
        elif operasi == '2':
            print(f"Hasil {bilangan1} - {bilangan2} =", kurang(bilangan1, bilangan2))
        elif operasi == '3':
            print(f"Hasil {bilangan1} * {bilangan2} =", kali(bilangan1, bilangan2))
        elif operasi == '4':
            print(f"Hasil {bilangan1} / {bilangan2} =", bagi(bilangan1, bilangan2))
    else:
        print('Mohon masukan angka!')