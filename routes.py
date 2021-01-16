from app.views import book_library_view, add_book_view, add_author_view, add_relation_view
from app.views import delete_book_view, delete_author_view, delete_relation_view, edit_book_view, edit_author_view
from app import app


@app.route("/")
def book_library():
    return book_library_view()


@app.route("/add/author/", methods=["GET", "POST"])
def add_author():
    return add_author_view()


@app.route("/add/book/", methods=["GET", "POST"])
def add_book():
    return add_book_view()


@app.route("/add/relation/", methods=["GET", "POST"])
def add_relation():
    return add_relation_view()


@app.route("/delete/book/<int:number>/", methods=["GET", "POST"])
def delete_book(number):
    return delete_book_view(number)


@app.route("/delete/author/<int:number>/", methods=["GET", "POST"])
def delete_author(number):
    return delete_author_view(number)


@app.route("/delete/relation/<int:number>", methods=["GET", "POST"])
def delete_relation(number):
    return delete_relation_view(number)


@app.route("/edit/book/<int:number>", methods=["GET", "POST"])
def edit_book(number):
    return edit_book_view(number)


@app.route("/edit/author/<int:number>", methods=["GET", "POST"])
def edit_author(number):
    return edit_author_view(number)


if __name__ == "__main__":
    app.run(debug=True)
