import pytest

from components.archive_category_alert_element import ArchiveCategoryAlertElement
from components.logout_alert_element import LogoutAlertElement


@pytest.fixture
def logout_alert(page):
    logout_alert = LogoutAlertElement(page)
    return logout_alert

@pytest.fixture
def archive_category_alert(page):
    archive_category_alert = ArchiveCategoryAlertElement(page)
    return archive_category_alert
