"""
Membuat perulangan dengan While
"""

jumlah_buku_yang_harus_dibaca = 10
total_jumlah_baca = 0
jumlah_buku_yang_sudah_dibaca = 0
print(f"Jumlah yang sudah dibaca {jumlah_buku_yang_sudah_dibaca} buah")
while total_jumlah_baca < jumlah_buku_yang_harus_dibaca * 2 :
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_yang_sudah_dibaca == 9:
        print(f"Buku ke {jumlah_buku_yang_sudah_dibaca} belum paham")

    else:
        jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca + 1
        print(f"Membaca dan memahami buku ke {jumlah_buku_yang_sudah_dibaca} buah")

print(f"Jumlah yang sudah dibaca dan dipahami {jumlah_buku_yang_sudah_dibaca} buah")
print(f"Telah mebaca sebanyak {total_jumlah_baca} kali")
print(f"Jumlah yang belum dibaca dan dipahami {jumlah_buku_yang_harus_dibaca - jumlah_buku_yang_sudah_dibaca} buah")


