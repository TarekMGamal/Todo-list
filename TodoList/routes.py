from TodoList import app
from flask import render_template
from TodoList.models import task

@app.route('/')
@app.route('/home')
def TodoList():
    todolist = task.query.all()
    return render_template('homepage.html' , todolist=todolist)
