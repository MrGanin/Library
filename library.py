import json

class Book:
    def __init__(self, title, author, year, status="в наличии"):
        self.id = id(self)
        self.title = title
        self.author = author
        self.year = year
        self.status = status

class Library:

    #Метод загрузки данных из json файла
    def load_data(self):
        try:
            with open('library.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = []
        return data

    #Метод сохранения данных в json файл
    def save_data(self, data):
        with open('library.json', 'w') as file:
            json.dump(data, file, indent=2)

    #Метод добавления книги
    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        data = self.load_data()
        book = {
                'id': new_book.id,
                'title': new_book.title,
                'author': new_book.author,
                'year': new_book.year,
                'status': new_book.status
            }
        data.append(book)
        self.save_data(data)
        print('Книга добавлена успешно.')

    #Метод удаления книги
    def remove_book(self, book_id):
        data = self.load_data()
        for book in data:
            if book['id'] == book_id:
                data.remove(book)
                self.save_data(data)
                print('Книга удалена успешно.')
                return
        print('Книга с указанным ID не найдена.')

    #Метод поиск книги
    def search_book(self, keyword):
        found_books = []
        for book in self.load_data():
            if keyword in [book['title'], book['author'], str(book['year'])]:
                found_books.append(book)
        return found_books

    #Метод отображения списка книг
    def display_all_books(self):
        if not self.load_data():
            print('В библиотеки нет книг')
        else:
            for book in self.load_data():
                print(f"ID: {book['id']}, Название: {book['title']}, Автор: {book['author']}, Год: {book['year']}, Статус: {book['status']}")

    #Метод изменения статуса
    def change_status(self, book_id, new_status):
        data = self.load_data()
        for book in data:
            if book['id'] == book_id:
                if book['status'] != new_status:
                    book['status'] = new_status
                    self.save_data(data)
                    break

                print('Книга находится в данном статусе')
                break
            print('Книга с указанным ID не найдена.')