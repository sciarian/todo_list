from project import db

class Thing_todo(db.Model):

    __tablename__ = "things todo"
    thing_todo = db.Column(db.String, primary_key = True)

    def __init__(self, thing_todo):
        self.thing_todo = thing_todo

    def __repr__(self):
        return '<title {}'.format(self.name)

