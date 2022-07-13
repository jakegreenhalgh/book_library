from models.author import Author
from models.book import Book

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("George R.R. Martin")
author_repository.save(author1)
author2 = Author("J.R Tolkein")
author_repository.save(author2)

author_repository.select_all()

book1 = Book("Game of Thrones", author1)
book_repository.save(book1)

book2 = Book("Fellowship of the Ring", author2)
book_repository.save(book2)
