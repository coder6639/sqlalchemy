from flask import render_template, redirect, request, url_for
from app.models import Book, Author, BookAuthors, add_data, edit_data
from forms.forms import BookForm, AuthorForm


def book_library_view():
    books = Book.query.all()
    return render_template("library.html", books=books)


def add_author_view():
    form = AuthorForm()
    authors = Author.query.all()
    if request.method == "POST":
        if form.validate_on_submit():
            add_data("author")
        return redirect(url_for("add_author"))
    return render_template("addauthor.html", form=form, authors=authors)


def add_book_view():
    form = BookForm()
    books = Book.query.all()
    if request.method == "POST":
        if form.validate_on_submit():
            add_data("book")
        return redirect(url_for("add_book"))
    return render_template("addbook.html", form=form, books=books)


def add_relation_view():
    authors = Author.query.all()
    books = Book.query.all()
    bookauthors = BookAuthors.query.all()
    if request.method == "POST":
        add_data("relation")
        return redirect(url_for("add_relation"))
    return render_template("bookauthors.html",
                           authors=authors,
                           books=books,
                           bookauthors=bookauthors)


def delete_book_view(number):
    book = Book.query.get(number)
    if request.method == "POST":
        book.delete()
        return redirect(url_for("add_book"))
    return render_template("delete.html", item=book)


def delete_author_view(number):
    author = Author.query.get(number)
    if request.method == "POST":
        author.delete()
        return redirect(url_for("add_author"))
    return render_template("delete.html", item=author)


def delete_relation_view(number):
    relation = BookAuthors.query.get(number)
    if request.method == "POST":
        relation.delete()
        return redirect(url_for("add_relation"))
    return render_template("delete.html", item=relation)


def edit_book_view(number):
    book = Book.query.get(number)
    form = BookForm()
    if request.method == "POST":
        edit_data(book, "book")
        return redirect(url_for("add_book"))
    return render_template("edit.html", book=book, form=form)


def edit_author_view(number):
    form = AuthorForm()
    author = Author.query.get(number)
    if request.method == "POST":
        edit_data(author, "author")
        return redirect(url_for("add_author"))
    return render_template("edit.html", author=author, form=form)
