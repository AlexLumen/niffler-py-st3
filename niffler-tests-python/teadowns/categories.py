import time

import pytest


@pytest.fixture
def delete_categories(request, envs, category_db, spend_data_for_add):
    def teardown():
        category_in_db = category_db.get_category_by_name(envs.username, spend_data_for_add.category.name)
        if category_in_db is not None:
            category_db.delete_category(category_in_db.id)
        category_in_db = category_db.get_category_by_name(envs.username,
                                                          f"{spend_data_for_add.category.name}_edited")
        if category_in_db is not None:
            category_db.delete_category(category_in_db.id)
    request.addfinalizer(teardown)


@pytest.fixture
def delete_category_with_spendings(request, envs, category_db, spends_client, spend_data_for_add, spend_db):
    def teardown():
        spends = spends_client.get_spends()
        for spend in spends:
            if spend.category.name == spend_data_for_add.category.name:
                spends_client.remove_spends(ids=[spend.id])
        category_in_db = category_db.get_category_by_name(envs.username, spend_data_for_add.category.name)
        category_db.delete_category(category_in_db.id)

    request.addfinalizer(teardown)

@pytest.fixture
def delete_category_with_edited_spendings(request, envs, category_db, spends_client, spend_data_for_edit, spend_db):
    def teardown():
        spends = spends_client.get_spends()
        for spend in spends:
            if spend.category.name == spend_data_for_edit.category.name:
                spends_client.remove_spends(ids=[spend.id])
        category_in_db = category_db.get_category_by_name(envs.username, spend_data_for_edit.category.name)
        category_db.delete_category(category_in_db.id)

    request.addfinalizer(teardown)

@pytest.fixture
def delete_category(request, envs, category_db, category_value):
    def teardown():
        category_in_db = category_db.get_category_by_name(envs.username, category_value)
        if category_in_db is not None:
            category_db.delete_category(category_in_db.id)

    request.addfinalizer(teardown)
