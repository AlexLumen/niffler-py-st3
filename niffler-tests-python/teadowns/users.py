import pytest


@pytest.fixture
def delete_user(request, user_db, authority_db, user_data):
    def teardown():
        user_in_db = user_db.get_user_by_username(user_data['username'])
        authority_db.delete_authority(user_in_db.id)
        user_db.delete_user_by_id(user_in_db.id)

    request.addfinalizer(teardown)
