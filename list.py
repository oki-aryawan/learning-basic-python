book_list = ['Narnia', 'One Piece', 'Naruto', 'GOT', 'Hentai', 'Lords of the Rings']
print('Show all books with for')
for book in book_list:
    print(book)


print('\nShow books with specific index')
print(book_list[2])
print(book_list[3])


print('\nShow books with for in range')
for i in range (0, len(book_list)):
    print(book_list[i])

#multiple date type in list
book_list = [1, 11.5, 'Game of Thrones', -100]
for book in book_list:
    print(book)

print('\nClear the entire list')
book_list.clear()
for i in range (0, len(book_list)):
    print(book_list[i])

print('\nReplace element')
book_list = ['Narnia', 'One Piece', 'Naruto', 'GOT', 'Hentai', 'Lords of the Rings']
book_list[3] = 'Fairy Tail'
for i in range (0, len(book_list)):
    print(book_list[i])

print('\nTake the element')
my_book = book_list.pop(2)
for i in range (0, len(book_list)):
    print(book_list[i])
print(f'\nMy on book from list: {my_book}')