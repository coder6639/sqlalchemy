from app import db
from datetime import datetime


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True)
    surname = db.Column(db.String(100), index=True)
    bookauthors = db.relationship("BookAuthors", backref="author", lazy="dynamic")

    def __str__(self):
        return f"<Author {self.name} {self.surname}>"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    year = db.Column(db.Integer, index=True)
    available = db.Column(db.Boolean, index=True)
    availability = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    bookauthors = db.relationship("BookAuthors", backref="book", lazy="dynamic")

    def __str__(self):
        return f"<Book {self.title}, {self.year}>"


class BookAuthors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
