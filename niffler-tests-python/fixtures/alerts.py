import pytest

from components.archive_category_alert_element import ArchiveCategoryAlertElement
from components.logout_alert_element import LogoutAlertElement


@pytest.fixture
def logout_alert(page):
    return LogoutAlertElement(page)


@pytest.fixture
def archive_category_alert(page):
    return ArchiveCategoryAlertElement(page)
