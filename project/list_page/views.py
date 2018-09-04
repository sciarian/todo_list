###########
# Imports #
###########
from flask import render_template, Blueprint

##########
# Config #
##########
base_blueprint = Blueprint('base', __name__, template_folder = 'templates')

##########
# Routes #
##########

@base_blueprint.route('/')
def index():
    return render_template('base.html')


