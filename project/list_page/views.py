###########
# Imports #
###########
from flask import render_template, Blueprint
from project.models import Thing_todo

##########
# Config #
##########
base_blueprint = Blueprint('base', __name__, template_folder = 'templates')

##########
# Routes #
##########

@base_blueprint.route('/')
def index():
    things_todo = Thing_todo.query.all()
    return render_template('base.html', todo_list=things_todo)
