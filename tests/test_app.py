from http import HTTPStatus


def test_read_root_should_return_OK_and_hello_world(client):
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    data = {
        'username': 'user',
        'email': 'email@gmail.com',
        'password': 'password',
    }
    expected_response = {
        'id': 1,
        'username': 'user',
        'email': 'email@gmail.com',
    }

    response = client.post('/users', json=data)

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == expected_response


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'user',
                'email': 'email@gmail.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'user',
            'email': 'email@gmail.com',
            'password': 'password',
            'id': 1,
        },
    )

    assert response.status_code == HTTPStatus.OK


def test_update_user_when_id_not_found(client):
    response = client.put(
        '/users/333',
        json={
            'username': 'user',
            'email': 'email@gmail.com',
            'password': 'password',
            'id': 1,
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted'}
