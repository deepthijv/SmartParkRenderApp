from flask import Blueprint, request, jsonify, redirect, url_for
from .extensions import db
from .models import User

main = Blueprint('main', __name__)

@main.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [{'id': user.id, 'username': user.username} for user in users]

    return jsonify(users=users_list)

@main.route('/', methods=['POST'])
def add_user():
    data = request.get_json()

    if 'username' not in data:
        return jsonify({'error': 'Missing username parameter'}), 400

    new_user = User(username=data['username'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User added successfully'}), 201

# Additional route to add a user using URL parameter
@main.route('/add/<username>', methods=['GET'])
def add_user_from_url(username):
    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("main.get_users"))
