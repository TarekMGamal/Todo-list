from TodoList import database

class task(database.Model):
    id = database.Column(database.Integer() , primary_key = True)
    todo = database.Column(database.String(length = 50) , nullable=False)
    isdone = database.Column(database.Boolean() , default = False , nullable=False)
    date = database.Column(database.DateTime() , nullable=False)
    def __repr__(self):
        return f'task {self.id}'
