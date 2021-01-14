from app import app, db
from app.models import Author, BookAuthors, Book

@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "author": Author,
        "book": Book,
        "bookauthors": BookAuthors
    }

