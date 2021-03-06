###########
# Imports #
###########

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

##########
# Config #
##########
app = Flask(__name__, instance_relative_config=True)#Grab instance relative 
                                                         #instance of flask pp
app.config.from_pyfile('flask.cfg')#Set configuration file for flask app                     

db = SQLAlchemy(app)              #Grab instance for database of flask app  

##############
# Blueprints #
##############

#Add blue print for todolist
from project.list_page.views import todolist_blueprint

#Register blue print
app.register_blueprint(todolist_blueprint)
