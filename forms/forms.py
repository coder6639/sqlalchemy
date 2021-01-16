from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    year = IntegerField("year", validators=[DataRequired()])
    available = BooleanField("available?", default="checked")
    availability = StringField("availability", validators=[DataRequired()])


class AuthorForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    surname = StringField("surname", validators=[DataRequired()])
