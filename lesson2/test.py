import pytest
from library import Library
from book import Book
library = Library()

def test_add_book():

    b = Book("hello","Avi")
    library.add_book(b)
    assert b in library.books

def test_add_user():
    library.add_user("test_user")
    assert "test_user" in library.users

def test_check_out_book_book_not_exist():
    b = Book("ggg", "Avi")
    with pytest.raises(ValueError):
      library.check_out_book("test_user",b)

def test_return_book_success():
    b = Book("ggg", "Avi")
    library.add_user("test_user")
    library.return_book("test_user",b)
    assert b.is_checked_out == False

def test_search_books_empty_result():
    library.add_book(Book("name","Rachel"))
    result = library.search_books("hhhh")
    assert result == []