from flask import Blueprint, jsonify, request
from models.user import User
from setup import session
from utils.errors import NotFoundError

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()

        first_name = data['first_name']
        last_name = data['last_name']
        age = data['age']

        user = User(first_name, last_name, age)
        session.add(user)
        session.commit()

        return jsonify({'message': 'user created successfully'}), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@users_bp.route('/users', methods=['GET'])
def get_all_users():
    try:
        raw_users = session.query(User).all()

        users = [format_user(user) for user in raw_users]

        session.close()

        return jsonify(users), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@users_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    try:
        user = session.query(User).get(id)

        if not user:
            raise  NotFoundError(f'user with id {id} does not exist')
        
        return jsonify(format_user(user)), 200
    except NotFoundError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@users_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user = session.query(User).get(id)
        
        if not user:
            raise ValueError(f'user with id {id} does not exist')

        data = request.get_json()

        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.age = data['age']

        session.commit()

        return jsonify({'message': 'user updated successfully'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@users_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = session.query(User).get(id)
        
        if not user:
            raise NotFoundError(f'user with id {id} does not exist')
        
        session.delete(user)
        session.commit()
        
        return jsonify({'message': 'user deleted successfully'}), 200
    except NotFoundError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@users_bp.route('/users/<int:id1>/<int:id2>', methods=['DELETE'])
def delete_many_users(id1, id2):
    responses = []
    for i in range(id1, id2 + 1):
        try:
          delete_user(i)
          responses.append(f"deleted {i}")
        except:
            print(f"something went wrong when deleting {i}")
    
    return jsonify({'message': responses}), 200

def format_user(user):
    return {'id': user.id, 'first_name': user.first_name, 'last_name': user.last_name, 'age': user.age}