import sys
import os


root_dir = os.path.dirname(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)


from fixtures.authorization import login_user, login_page
from fixtures.person import person_generator, user_data
from fixtures.spendings import (spends_client, currency, create_category,
                        create_second_category, category_value,
                        add_spending_page, spend_data_for_add,
                        add_spend, spend_data_for_edit)
from fixtures.profile import open_profile_page, profile_page
from fixtures.alerts import archive_category_alert, logout_alert
from fixtures.header_element import header_element
from fixtures.main_page import main_page
from fixtures.navbar import navbar_element
from fixtures.registration import registration_page
from fixtures.soap_fixtures import (api_session, api_wookie_session,
                            api_destruction_session, api_module_session,
                            soap_session)

__all__ = [

    'login_user',
    'login_page',

    'person_generator',
    'user_data',


    'spends_client',
    'currency',
    'create_category',
    'create_second_category',
    'category_value',
    'add_spending_page',
    'spend_data_for_add',
    'add_spend',
    'spend_data_for_edit',

    'open_profile_page',
    'profile_page',

    'archive_category_alert',
    'logout_alert',

    'header_element',


    'main_page',

    'navbar_element',

    'registration_page',

    'api_session',
    'api_wookie_session',
    'api_destruction_session',
    'api_module_session',
    'soap_session'
]
