import pytest


@pytest.fixture
def delete_spending(request, main_page, page, spend_data_for_add, spends_client):
    def teardown():
        identify = main_page.get_id_attribute_created_spending(spend_data_for_add.category.name)
        spends_client.remove_spends(ids=identify)
        categories = spends_client.get_categories()
        for category in categories:
            if category.name == spend_data_for_add.category.name:
                category.archived = True
                category_dict = category.model_dump()
                spends_client.update_category(category_dict)

    request.addfinalizer(teardown)


@pytest.fixture
def archive_category(request, spend_data_for_add, spends_client):
    def teardown():
        categories = spends_client.get_categories()
        for category in categories:
            if category.name in [spend_data_for_add.category.name, f"{spend_data_for_add.category.name}_edited"]:
                category.archived = True
                category_dict = category.model_dump()
                spends_client.update_category(category_dict)

    request.addfinalizer(teardown)
