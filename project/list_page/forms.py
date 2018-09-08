from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class AddTodoItemForm(FlaskForm):
    todo_item = StringField("What else will you do today: ", validators=[DataRequired()])

