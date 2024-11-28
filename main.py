from library import Library

#Главная функция
def main():

    library = Library()

    while True:
        try:
            print('\n1. Добавить книгу')
            print('2. Удалить книгу')
            print('3. Найти книгу')
            print('4. Отобразить все книги')
            print('5. Изменить статус книги')
            print('6. Выйти')
            choice = int(input('Введите номер действия: '))

            if choice == 1:
                title = input('Введите название книги: ')
                author = input('Введите автора книги: ')
                year = int(input('Введите год издания: '))
                library.add_book(title, author, year)

            elif choice == 2:
                book_id = int(input('Введите ID книги для удаления: '))
                library.remove_book(book_id)

            elif choice == 3:
                search_key = input('Введите один атрибут (название, автор, год издания): ')
                books = library.search_book(search_key)
                if not books:
                    print('По вашему запросу ничего не найдено')
                else:
                    for book in books:
                        print(f"ID: {book['id']} Название: {book['title']}, Автор: {book['author']}, Год издания: {book['year']}, Статус: {book['status']}")

            elif choice == 4:
                library.display_all_books()

            elif choice == 5:
                book_id = int(input('Введите ID книги для изменения статуса: '))
                new_status = input('Введите новый статус (в наличии, выдана): ')

                if new_status.lower() in ['в наличии', 'выдана']:
                    library.change_status(book_id, new_status)
                else:
                    raise ValueError

            elif choice == 6:
                break

            else:
                print('Некорректный выбор, попробуйте снова.')

        except ValueError:
            print('Некорректное значение, попробуйте снова.')

if __name__ == "__main__":
    main()