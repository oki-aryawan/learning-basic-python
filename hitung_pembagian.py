print('Menghitung Nilai Pembagian')
total = 0

x = int(input('Pembagi1: '))
y = int(input('Pembagi2: '))
range_angka = int(input('Range angka: '))
for angka in range(1, range_angka):
    if angka % x == 0 and angka % y == 0:
        print(f'Nilai {angka}')
        total = total + angka

print (f'Total = {total}')




