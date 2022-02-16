sudut = int (input('Sudut: '))

print(f'Sudut = {sudut} derajat')
print('\nArah')
if(0<sudut<45 or 315<sudut<=360):
    print("Utara")
elif(sudut==45):
    print("Timur Laut")
elif(45<sudut<134):
    print("Timur")
elif(sudut==135):
    print("Tenggara")
elif(135<sudut<225):
    print("Selatan")
elif(sudut==225):
    print("Barat Daya")
elif(225<sudut<315):
    print("Barat")
elif(sudut==315):
    print("Barat Laut")
