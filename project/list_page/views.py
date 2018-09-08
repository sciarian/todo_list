###########
# Imports #
###########
from flask import render_template, Blueprint, request, redirect, url_for
from project.models import Thing_todo
from project.list_page.forms import AddTodoItemForm 
from project import db

##########
# Config #
##########
todolist_blueprint = Blueprint('todolist', __name__, template_folder = 'templates')

##########
# Routes #
##########

@todolist_blueprint.route('/')
def index():
    things_todo = Thing_todo.query.all()
    return render_template('todo_list.html', todo_list=things_todo)
        

#methods - This determines what HTTP methods this route will respond to. in this case
#          it will respond the GET and POST methods
@todolist_blueprint.route('/add_item', methods = ['GET', 'POST'])
def add_todo_item():
    form = AddTodoItemForm(request.form)    #TODO Error not defined

    ### CASE: POST
    #POST the new todo list item that the user has created to the todo list html page
    if request.method == 'POST':
        if form.validate_on_submit():
            new_thing_todo = Thing_todo(form.todo_item.data)
            db.session.add(new_thing_todo)
            db.session.commit()
            return redirect(url_for('todolist.index'))
 
    ###CASE: GET
    #Send used the add todo item template with a form to GET the
    return render_template('add_todo_item.html', form = form)
