class Book:

    def __init__(self, title=None, writer=None, genres=None):
        self.title = title
        self.writer = writer
        self.genres = genres
        self.pages = 100

        print(self.title, self.writer, self.genres, self.pages)

book = Book()
book.title = "Pupung Collections"
book.writer = "Tonton Young"
book.genres = ["Family", "Comedy"]

print(book.title, book.writer, book.genres, book.pages)
