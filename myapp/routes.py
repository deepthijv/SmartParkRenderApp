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

    # Check for the required parameters
    required_params = ['firstname', 'lastname', 'phone', 'email']
    missing_params = [param for param in required_params if param not in data]

    if missing_params:
        return jsonify({'error': f'Missing parameters: {", ".join(missing_params)}'}), 400

    # Extract user information from the request
    firstname = data['firstname']
    lastname = data['lastname']
    phone = data['phone']
    email = data['email']

    # Create a new user with the provided information
    new_user = User(
        firstname=firstname,
        lastname=lastname,
        phone=phone,
        email=email
    )

    # Add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User added successfully'}), 200
