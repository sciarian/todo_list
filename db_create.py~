#Imports
from project import db
from project.models import Thing_todo

#Create database
db.create_all()

#Craete things to add to things todo database
thing1 = Thing_todo("Testing database...")
thing2 = Thing_todo("If you can see this the database works")

#Insert things into the database
db.session.add(thing1)
db.session.add(thing2)

#Commit changes to the database
db.session.commit()
