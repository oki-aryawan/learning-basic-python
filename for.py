book = 10
readed_book = 0

print("Baca semua buku")
print(f"Jumlah buku adalah {book} buah")
print(f"Buku yang sudah dibaca {readed_book} buah")

for readed_book in range (0, 10):
    readed_book = readed_book + 1
    print(f"Membaca buku ke {readed_book}")

#print(f"Buku yang sudah dibaca {jumlah_buku_dibaca} buah")

if readed_book == book :
    print("Telah membaca semua buku")
