import datetime
from flask.helpers import url_for
from werkzeug.utils import redirect
from TodoList import app
from flask import render_template , request
from TodoList.models import task
from TodoList import database

@app.route('/')
@app.route('/home')
def TodoList():
    todolist = task.query.all()
    return render_template('homepage.html' , todolist=todolist)


@app.route('/add', methods=['POST' , 'GET'])
def addtask():
    todo = request.form.get("newtodo")
    dateday = request.form.get("newdateday")
    datemonth = request.form.get("newdatemonth")
    dateyear = request.form.get("newdateyear")
    date = datetime.datetime(int(dateyear) , int(datemonth) , int(dateday))
    new_todo = task(todo=todo, date=date , isdone=False)
    database.session.add(new_todo)
    database.session.commit()
    return redirect(url_for('TodoList'))


@app.route('/edit/<int:task_id>', methods=['POST' , 'GET'])
def edittask(task_id):
    todo = request.form.get("edittodo")
    dateday = request.form.get("editday")
    datemonth = request.form.get("editmonth")
    dateyear = request.form.get("edityear")
    date = datetime.datetime(int(dateyear) , int(datemonth) , int(dateday))
    done = request.form.get("editisdone")
    if done == 'on':
        done = True
    else:
        done = False
    existingtask = task.query.filter_by(id=task_id).first()
    existingtask.todo = todo
    existingtask.date = date
    existingtask.isdone = done
    database.session.commit()
    return redirect(url_for('TodoList'))


@app.route('/delete/<int:task_id>', methods=['POST' , 'GET'])
def deletetask(task_id):
    existingtask = task.query.filter_by(id=task_id).first()
    database.session.delete(existingtask)
    database.session.commit()
    return redirect(url_for('TodoList'))

