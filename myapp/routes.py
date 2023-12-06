from flask import Blueprint, request, jsonify, redirect, url_for
from .extensions import db
from .models import User

main = Blueprint('main', __name__)

@main.route('/users/<email>', methods=['GET'])
def get_users(email):
    user = User.query.filter_by(email=email).first()

    if user:
        # Return the first user directly
        user_dict = {'id': user.id, 'firstname': user.firstname,'lastname':user.lastname,'phone':user.phone,'email':user.email}
        return jsonify(user_dict)

@main.route('/adduser/', methods=['POST'])
def add_user():
        data = request.get_json()

        if 'username' not in data:
            return jsonify({'error': 'Missing username parameter'}), 400

        # Extract additional user information from the request
        id = data.get('id', '')
        firstname = data.get('firstname', '')
        lastname = data.get('lastname', '')
        phone = data.get('phone', '')
        email = data.get('email', '')

        # Create a new user with the provided information
        new_user = User(
            id=id,
            firstname=firstname,
            lastname=lastname,
            phone=phone,
            email=email
        )

        # Add the new user to the database
        db.session.add(new_user)
        db.session.commit()