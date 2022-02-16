print('Verifikasi Bilangan Phytagoras')
angka1 = int(input('Masukkan angka-1: '))
angka2 = int(input('Masukkan angka-2: '))
angka3 = int(input('Masukkan angka-3: '))

if ((angka1 * angka1) + (angka2 * angka2) == (angka3 * angka3)):
    print('Phytagoras')
else:
    print('Bukan Phytagoras')
