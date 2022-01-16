jumlah_buku = 10
jumlah_buku_dibaca = 0

print("Baca semua buku")
print(f"Jumlah buku adalah {jumlah_buku} buah")
print(f"Buku yang sudah dibaca {jumlah_buku_dibaca} buah")

for jumlah_buku_dibaca in range (0,10):
    jumlah_buku_dibaca = jumlah_buku_dibaca + 1
    print(f"Membaca buku ke {jumlah_buku_dibaca}")

#print(f"Buku yang sudah dibaca {jumlah_buku_dibaca} buah")

if jumlah_buku_dibaca == jumlah_buku :
    print("Telah membaca semua buku")
