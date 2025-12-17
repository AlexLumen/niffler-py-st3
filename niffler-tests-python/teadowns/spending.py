import pytest

from Pages.MainPage import MainPage


@pytest.fixture
def delete_spending(request, browser, category_value, spends_client):
    def teardown():
        main_page = MainPage(browser)
        identify = main_page.get_id_attribute_created_spending(category_value)
        print(identify)
        spends_client.remove_spends(ids=identify)
        categories = spends_client.get_categories()
        for category in categories:
            if category['name'] == category_value:
                category['archived'] = True
                spends_client.update_category(category)

    request.addfinalizer(teardown)


