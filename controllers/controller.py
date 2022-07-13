from flask import Flask, render_template, Blueprint, redirect, request
from repositories import author_repository
from repositories import book_repository
from models.book import Book

books_blueprint = Blueprint("books",__name__)

# INDEX
@books_blueprint.route("/books")
def tasks():
    # Get tasks from the DB
    books = book_repository.select_all()
    # Pass the tasks to the template
    return render_template("books/index.html", all_books=books)

# delete books
@books_blueprint.route("/books/<id>/delete", methods=["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect ("/books")

@books_blueprint.route("/books/new", methods = ['GET'])
def new_book():
    authors = author_repository.select_all()
    return render_template("books/new.html", all_authors = authors)

@books_blueprint.route("/books", methods = ["POST"])
def create():
    title = request.form['title']
    author_id = request.form['author_id']
    author = author_repository.select(author_id)
    book = Book(title, author)
    book_repository.save(book)
    return redirect("/book")

@books_blueprint.route("/books/<id>")
def show(id):
    book = book_repository.select(id)
    return render_template("books/show.html", book = book)
