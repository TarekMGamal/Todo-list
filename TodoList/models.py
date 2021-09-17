from TodoList import database

class task(database.Model):
    id = database.Column(database.Integer() , primary_key = True)
    todo = database.Column(database.String(length = 50))
    isdone = database.Column(database.Boolean() , default = False)
    date = database.Column(database.DateTime())
    def __repr__(self):
        return f'task {self.id}'
