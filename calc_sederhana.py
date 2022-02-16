c = 'N'
d = 'Y'
mulai = str(input('Mulai? Y/N '))
while (mulai == d):
    bil1 = int(input('Masukkan nilai 1: '))
    bil2 = int(input('Masukkan nilai 2: '))
    print(bil1 + bil2)
    lanjut = str(input('Lanjut? Y/N '))
    if (lanjut == c):
        break
