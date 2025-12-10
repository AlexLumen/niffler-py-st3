# @pytest.fixture(scope='function')
# def logout(request, user_creds, browser):
#     def teardown():
#         navbar = NavbarElement(browser)
#         header_element = HeaderElement(browser)
#         logout_alert_element = LogoutAlertElement(browser)
#         header_element.click_person_icon()
#         navbar.click_sign_out_button()
#         logout_alert_element.click_logout_button()
#     request.addfinalizer(teardown)
