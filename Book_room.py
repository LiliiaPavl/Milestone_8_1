class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

    def get_category(self):
        return self.category

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.category}')"

class Shelf:
    def __init__(self, category):
        self.category = category
        self.books = []

    def add_book(self, book):
        if book.get_category() == self.category:
            self.books.append(book)

    def get_books(self):
        return self.books

    def __repr__(self):
        return f"Shelf('{self.category}', {self.books})"

class Room:
    def __init__(self):
        self.shelves = []

    def add_shelf(self, shelf):
        self.shelves.append(shelf)

    def organize_books(self, books):
        for book in books:
            placed = False
            for shelf in self.shelves:
                if book.get_category() == shelf.category:
                    shelf.add_book(book)
                    placed = True
                    break
            if not placed:
                new_shelf = Shelf(book.get_category())
                new_shelf.add_book(book)
                self.add_shelf(new_shelf)

    def __repr__(self):
        return f"Room({self.shelves})"

books = {
    Book("І будуть люди", "Анатолій Дімаров", "класика"),
    Book("Конотопська відьма", "Григорій Квітка-Основ'яненко", "класика"),
    Book("Гаррі Поттер", "Джоан Ролінг", "фентезі"),
    Book("Схід українського сонця", "Катерина Зарембо", "історія"),
    Book("Стародавня історія України", "Леонід Залізняк", "історія")
}

room = Room()
room.organize_books(books)
print(room)