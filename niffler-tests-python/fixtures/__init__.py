import sys
import os


root_dir = os.path.dirname(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)


from .authorization import login_user, login_page
from .person import person_generator, user_data
from .spendings import (spends_client, currency, create_category,
                        create_second_category, category_value,
                        add_spending_page, spend_data_for_add,
                        add_spend, spend_data_for_edit)
from .profile import open_profile_page, profile_page
from .alerts import archive_category_alert, logout_alert
from .header_element import header_element
from .main_page import main_page
from .navbar import navbar_element
from .registration import registration_page
from .soap_fixtures import (api_session, api_wookie_session,
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
