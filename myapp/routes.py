from flask import Blueprint, redirect, url_for,jsonify

from .extensions import db
from .models import User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    users = User.query.all()
    users_list = [{'id': user.id, 'username': user.username} for user in users]

    # Return the users as JSON
    return jsonify(users=users_list)

@main.route('/add/<username>')
def add_user(username):
    db.session.add(User(username=username))
    db.session.commit()
    return redirect(url_for("main.index"))