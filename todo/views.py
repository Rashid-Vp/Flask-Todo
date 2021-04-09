from flask import Blueprint, render_template, request, jsonify, flash
from flask_login import login_user, login_required, logout_user, current_user
from .models import Todo
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        todo = request.form.get('todo')
        new_todo = Todo(text=todo, user_id=current_user.id)
        db.session.add(new_todo)
        db.session.commit()
    return render_template("index.html", user=current_user)

@views.route('/remove_todo', methods=['POST'])
def remove_todo():
    todo = json.loads(request.data)
    todoId = todo['todoId']
    todo = Todo.query.get(todoId)
    if todo:
        if todo.user_id == current_user.id:
            db.session.delete(todo)
            db.session.commit()
    return jsonify({})