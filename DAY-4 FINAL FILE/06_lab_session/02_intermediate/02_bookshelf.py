"""
Final Project: Bookshelf Management System

In this project, you will manage a fixed-length bookshelf that can hold up to 10 books.

A book has the following attributes:
    - `name` (str): The name of the book.
    - `author` (str): The author of the book.
    - `genres` (set[str]): A set of genres associated with the book.

The player is provided with the following options:

1. **Add New Book**
    - Allow the user to provide the name, author, and genres for a new book.
    - If a book with the same name, author, and genres already exists in the bookshelf, display a warning and don't add the book.
    - If the bookshelf is full (already contains 10 books), display a warning and don't add the book.

2. **Remove Book**
    - Allow the user to search for a book by its name and remove it.
    - If the book is not in the bookshelf (based on the name), display a warning and don't remove anything.

3. **Get All Names**
    - Display the names of all books currently in the bookshelf.

4. **Get All Genres**
    - Display a list of all unique genres currently present in the bookshelf.

5. **Get All Authors**
    - Display a list of all unique authors currently present in the bookshelf.

6. **Get Book**
    - Given the name of a book, find it in the bookshelf and print its details (name, author, genres).
    - If the book is not in the bookshelf, display a warning.

7. **Get Books by Genre**
    - Given a genre input, display all books that have that genre.
    - If the user provides an invalid genre (no books match), display a warning.

8. **Get Books by Author**
    - Given an author's name, display all books written by that author.
    - If the user provides an invalid author (no books match), display a warning.

9. **Exit**
    - End the program.

In summary, this system allows users to manage a bookshelf by adding/removing books, listing books by name, genre, or author, and viewing book details.
"""

class Book:
    def __init__(self, name: str, author: str, genres: set[str]):
        """
        Initializes a new book with name, author, and genres.

        :param name: The name of the book.
        :param author: The author of the book.
        :param genres: A set of genres the book belongs to.
        """
        self.name = name
        self.author = author
        self.genres = genres

    def __str__(self) -> str:
        """
        Returns a string representation of the book with name, author, and genres.
        """
        return f"Name: {self.name}, Author: {self.author}, Genres: {', '.join(self.genres)}"


class Bookshelf:
    def __init__(self):
        """
        Initializes an empty bookshelf with a fixed capacity of 10 books.
        """
        self.books = []

    def add_book(self, book: Book):
        """
        Adds a book to the bookshelf if it's not already in the bookshelf
        and if there is space available.

        :param book: The book to add to the bookshelf.
        """
        pass  # Implement logic to check if book already exists or if shelf is full.

    def remove_book(self, name: str):
        """
        Removes a book by name from the bookshelf.

        :param name: The name of the book to remove.
        """
        pass  # Implement logic to search and remove a book by name.

    def get_all_names(self):
        """
        Prints the names of all books in the bookshelf.
        """
        pass  # Implement logic to print book names.

    def get_all_genres(self):
        """
        Returns a list of all unique genres in the bookshelf.
        """
        pass  # Implement logic to collect and return all genres.

    def get_all_authors(self):
        """
        Returns a list of all unique authors in the bookshelf.
        """
        pass  # Implement logic to collect and return all authors.

    def get_book(self, name: str):
        """
        Prints the details of the book by name (name, author, genres).

        :param name: The name of the book to search for.
        """
        pass  # Implement logic to search for a book by name and print its details.

    def get_books_by_genre(self, genre: str):
        """
        Prints all books in the bookshelf that match the provided genre.

        :param genre: The genre to search for.
        """
        pass  # Implement logic to filter books by genre.

    def get_books_by_author(self, author: str):
        """
        Prints all books in the bookshelf that match the provided author.

        :param author: The author to search for.
        """
        pass  # Implement logic to filter books by author.


def main():
    bookshelf = Bookshelf()

    while True:
        print("\n--- Bookshelf Management System ---")
        print("1. Add new book")
        print("2. Remove book")
        print("3. Get all names")
        print("4. Get all genres")
        print("5. Get all authors")
        print("6. Get book")
        print("7. Get books by genre")
        print("8. Get books by author")
        print("9. Exit")
        choice = input("Please select an option: ")

        if choice == '1':
            # Add new book: get name, author, genres from user
            pass  # Implement logic to add a new book

        elif choice == '2':
            # Remove book: get book name from user
            pass  # Implement logic to remove a book

        elif choice == '3':
            # Get all book names
            pass  # Implement logic to display all book names

        elif choice == '4':
            # Get all genres
            pass  # Implement logic to display all genres

        elif choice == '5':
            # Get all authors
            pass  # Implement logic to display all authors

        elif choice == '6':
            # Get book details by name
            pass  # Implement logic to display book details by name

        elif choice == '7':
            # Get books by genre
            pass  # Implement logic to display books by genre

        elif choice == '8':
            # Get books by author
            pass  # Implement logic to display books by author

        elif choice == '9':
            print("Exiting the program.")
            break  # Exit the program

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
