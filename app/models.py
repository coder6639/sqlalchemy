from app import db
from flask import request
from forms.forms import BookForm


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    surname = db.Column(db.String(100), index=True)
    bookauthors = db.relationship(
        "BookAuthors", backref="author", lazy="dynamic")

    def __str__(self):
        return f"<Author {self.name} {self.surname}>"

    def delete(self):
        relations = self.bookauthors.all()
        for relation in relations:
            db.session.delete(relation)
        db.session.delete(self)
        db.session.commit()


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    year = db.Column(db.Integer, index=True)
    available = db.Column(db.Boolean, index=True)
    availability = db.Column(db.String, index=True)
    bookauthors = db.relationship(
        "BookAuthors", backref="book", lazy="dynamic")

    def __str__(self):
        return f"<Book {self.title}, {self.year}>"

    def delete(self):
        relations = self.bookauthors.all()
        for relation in relations:
            db.session.delete(relation)
        db.session.delete(self)
        db.session.commit()


class BookAuthors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __str__(self):
        return f"<Relation {self.id} - Book id: {self.book_id}, " \
               f"Author id: {self.author_id}>"

    def delete(self):
        db.session.delete(self)
        db.session.commit()


def add_data(form_type):
    if form_type == "book":
        form = BookForm()
        book = Book(
            title=request.form["title"],
            year=request.form["year"],
            available=form.data.get("available"),
            availability=request.form["availability"]
        )
        db.session.add(book)

    elif form_type == "author":
        author = Author(name=request.form["name"],
                        surname=request.form["surname"])
        db.session.add(author)

    elif form_type == "relation":
        book = request.form["books"]
        author = request.form["authors"]
        relation = BookAuthors(book_id=book, author_id=author)
        db.session.add(relation)

    db.session.commit()


def edit_data(item, form_type):
    if form_type == "book":
        form = BookForm()
        item.title = request.form["title"]
        item.year = request.form["year"]
        item.available = form.data.get("available")
        item.availability = request.form["availability"]

    elif form_type == "author":
        item.name = request.form["name"]
        item.surname = request.form["surname"]

    db.session.commit()
