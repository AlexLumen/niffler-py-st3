import pytest


@pytest.fixture
def archive_category(request, browser, category_value, spends_client):
    def teardown():
        categories = spends_client.get_categories()
        for category in categories:
            if category.name in [category_value, f"{category_value}_edited"]:
                category.archived = True
                spends_client.update_category(category)

    request.addfinalizer(teardown)


@pytest.fixture
def delete_category(request, envs, category_db, category_value):
    def teardown():
        category_in_db = category_db.get_category_by_name(envs.username, category_value)
        category_db.delete_category(category_in_db.id)

    request.addfinalizer(teardown)
