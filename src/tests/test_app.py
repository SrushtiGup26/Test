import pytest
from app import create_app, db
from app.models import Message

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_get_messages(client):
    rv = client.get('/messages')
    assert rv.status_code == 200

def test_post_message(client):
    rv = client.post('/messages', json={'content': 'You have won a free prize!'})
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['spam'] == True