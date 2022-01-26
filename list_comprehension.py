a = [-2, -10, -3, -4, 2, 5, 3, 6, 7]
negatif = [i
           for i in a
           if i < 0]
positif = [i
           for i in a
           if i > 0]

positif.sort(reverse=True)
negatif.sort()
print(f'nilai negatif: {negatif}')
print(f'nilai positif: {positif}')

c = [1, 2, 3, 4, 5, 6, 7, 8]

b = ['genap' if i % 2 == 0 else 'ganjil' for i in c]
print('\n')
print(c)
print(b)