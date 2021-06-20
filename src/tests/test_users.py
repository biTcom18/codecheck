# src/tests/test_users.py

import json


def test_add_user(test_app, test_database):
    client = test_app.test_client()
    resp = client.post(
        '/users',
        data=json.dumps({
            'username': 'ivan',
            'email': 'nabei@bitcom.info'
        }),
        context_type='application/json',
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert 'nabei@bitcom.info was added' in data['message']
