"""
Membuat perulangan dengan While
"""

book = 10
read_count = 0
readed_book = 0
print(f"Jumlah yang sudah dibaca {readed_book} buah")
while read_count < book * 2 :
    read_count = read_count + 1
    if readed_book == 9:
        print(f"Buku ke {readed_book} belum paham")

    else:
        readed_book = readed_book + 1
        print(f"Membaca dan memahami buku ke {readed_book} buah")

print(f"Jumlah yang sudah dibaca dan dipahami {readed_book} buah")
print(f"Telah mebaca sebanyak {read_count} kali")
print(f"Jumlah yang belum dibaca dan dipahami {book - readed_book} buah")


