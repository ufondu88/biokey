import pytest
from main import app
from models.user import User
from unittest.mock import patch

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


@patch('routes.users.session')
def test_create_user_with_bad_first_name(mock_session, client):
    data = {
        'first_name': 'J',
        'last_name': 'Doe',
        'age': 30
    }
    response = client.post('/users', json=data)

    assert response.status_code == 400
    assert 'first_name must be at least 2' in response.json['error']

@patch('routes.users.session')
def test_create_user_with_empty_first_name(mock_session, client):
    data = {
        'first_name': '',
        'last_name': 'Doe',
        'age': 30
    }
    response = client.post('/users', json=data)

    assert response.status_code == 400
    assert 'first_name cannot be empty' in response.json['error']

@patch('routes.users.session')
def test_create_user_with_bad_last_name(mock_session, client):
    data = {
        'first_name': 'John',
        'last_name': 'D',
        'age': 30
    }
    response = client.post('/users', json=data)

    assert response.status_code == 400
    assert 'last_name must be at least 2' in response.json['error']

@patch('routes.users.session')
def test_create_user_with_empty_last_name(mock_session, client):
    data = {
        'first_name': 'John',
        'last_name': '',
        'age': 30
    }
    response = client.post('/users', json=data)

    assert response.status_code == 400
    assert 'last_name cannot be empty' in response.json['error']

@patch('routes.users.session')
def test_create_user_with_bad_age(mock_session, client):
    data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'age': "30"
    }
    response = client.post('/users', json=data)

    assert response.status_code == 400
    assert 'age must be a number' in response.json['error']

@patch('routes.users.session')
def test_create_user_with_negative_age(mock_session, client):
    data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'age': -2
    }
    response = client.post('/users', json=data)

    assert response.status_code == 400
    assert 'age cannot be negative' in response.json['error']

@patch('routes.users.session')
def test_create_user(mock_session, client):
    data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 30
    }
    response = client.post('/users', json=data)

    mock_session.add.assert_called_once()
    mock_session.commit.assert_called_once()

    assert response.status_code == 201
    assert 'user created successfully' in response.json['message']

@patch('routes.users.session')
def test_get_all_users(mock_session, client):
    mock_session.query.return_value.all.return_value = [
        User(first_name='John', last_name='Doe', age=30),
        User(first_name='Jane', last_name='Doe', age=25)
    ]

    response = client.get('/users')

    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) == 2

@patch('routes.users.session')
def test_get_all_users_empty(mock_session, client):
    mock_session.query.return_value.all.return_value = []

    response = client.get('/users')

    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert len(response.json) == 0

@patch('routes.users.session')
def test_get_user(mock_session, client):
    user = User(first_name='John', last_name='Doe', age=30)
    mock_session.query.return_value.get.return_value = user

    response = client.get('/users/1')

    assert response.status_code == 200
    assert response.json['first_name'] == 'John'
    assert response.json['last_name'] == 'Doe'
    assert response.json['age'] == 30

@patch('routes.users.session')
def test_get_user_does_not_exist(mock_session, client):
    mock_session.query.return_value.get.return_value = None

    response = client.get('/users/1')

    assert response.status_code == 404
    assert "does not exist" in response.json['error']

@patch('routes.users.session')
def test_update_user_with_bad_first_name(mock_session, client):
    user = User(first_name='John', last_name='Doe', age=30)
    mock_session.query.return_value.get.return_value = user

    data = {
        'first_name': 'J',
        'last_name': 'Doe',
        'age': 25
    }
    response = client.put('/users/1', json=data)

    assert response.status_code == 400
    assert 'first_name must be at least 2' in response.json['error']

@patch('routes.users.session')
def test_update_user_with_empty_first_name(mock_session, client):
    user = User(first_name='John', last_name='Doe', age=30)
    mock_session.query.return_value.get.return_value = user

    data = {
        'first_name': '',
        'last_name': 'Doe',
        'age': 25
    }
    response = client.put('/users/1', json=data)

    assert response.status_code == 400
    assert 'first_name cannot be empty' in response.json['error']

@patch('routes.users.session')
def test_update_user_with_bad_last_name(mock_session, client):
    user = User(first_name='John', last_name='Doe', age=30)
    mock_session.query.return_value.get.return_value = user

    data = {
        'first_name': 'Jane',
        'last_name': 'D',
        'age': 25
    }
    response = client.put('/users/1', json=data)

    assert response.status_code == 400
    assert 'last_name must be at least 2' in response.json['error']

@patch('routes.users.session')
def test_update_user_with_empty_last_name(mock_session, client):
    user = User(first_name='John', last_name='Doe', age=30)
    mock_session.query.return_value.get.return_value = user

    data = {
        'first_name': 'Jane',
        'last_name': '',
        'age': 25
    }
    response = client.put('/users/1', json=data)

    assert response.status_code == 400
    assert 'last_name cannot be empty' in response.json['error']

@patch('routes.users.session')
def test_update_user_with_bad_age(mock_session, client):
    user = User(first_name='John', last_name='Doe', age=30)
    mock_session.query.return_value.get.return_value = user

    data = {
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': "25"
    }
    response = client.put('/users/1', json=data)

    assert response.status_code == 400
    assert 'age must be a number' in response.json['error']

@patch('routes.users.session')
def test_update_user_with_negative_age(mock_session, client):
    user = User(first_name='John', last_name='Doe', age=30)
    mock_session.query.return_value.get.return_value = user

    data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'age': -1
    }
    response = client.put('/users/1', json=data)

    assert response.status_code == 400
    assert 'age cannot be negative' in response.json['error']


@patch('routes.users.session')
def test_update_user(mock_session, client):
    user = User(first_name='John', last_name='Doe', age=30)
    mock_session.query.return_value.get.return_value = user

    data = {
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': 25
    }
    response = client.put('/users/1', json=data)
    mock_session.commit.assert_called_once()

    assert response.status_code == 200
    assert 'user updated successfully' in response.json['message']
    assert user.first_name == 'Jane'
    assert user.age == 25

@patch('routes.users.session')
def test_delete_user(mock_session, client):
    user = User(first_name='John', last_name='Doe', age=30)
    mock_session.query.return_value.get.return_value = user

    response = client.delete('/users/1')
    mock_session.delete.assert_called_once_with(user)
    mock_session.commit.assert_called_once()

    assert response.status_code == 200
    assert 'user deleted successfully' in response.json['message']