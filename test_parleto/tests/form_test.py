from test_parleto.pages.form_page import *
from test_parleto.base import BaseTest


class TestsForm(BaseTest):

    def test_submit_button_without_data(self):
        FormPage(self.driver).click_submit_button()
        FormPage(self.driver).info_submit_button()

    def test_submit_form_successful(self):
        FormPage(self.driver).send_name()
        FormPage(self.driver).send_last_name()
        FormPage(self.driver).send_pesel()
        FormPage(self.driver).send_email()
        FormPage(self.driver).send_date()
        FormPage(self.driver).send_password()
        FormPage(self.driver).send_password_confirm()
        FormPage(self.driver).click_submit_button()
        FormPage(self.driver).popup_window()

    def test_submit_form_without_name(self):
        FormPage(self.driver).send_pesel()
        FormPage(self.driver).send_email()
        FormPage(self.driver).send_date()
        FormPage(self.driver).send_password()
        FormPage(self.driver).send_password_confirm()
        FormPage(self.driver).click_submit_button()
        FormPage(self.driver).without_one_data()

    def test_submit_form_without_password(self):
        FormPage(self.driver).send_name()
        FormPage(self.driver).send_last_name()
        FormPage(self.driver).send_pesel()
        FormPage(self.driver).send_email()
        FormPage(self.driver).send_date()
        FormPage(self.driver).click_submit_button()
        FormPage(self.driver).without_two_data()

    # this test is not supposed to work (yet it works)
    def test_submit_form_different_passwords(self):
        FormPage(self.driver).send_name()
        FormPage(self.driver).send_last_name()
        FormPage(self.driver).send_pesel()
        FormPage(self.driver).send_email()
        FormPage(self.driver).send_date()
        FormPage(self.driver).send_password()
        FormPage(self.driver).send_password_different()
        FormPage(self.driver).click_submit_button()
        FormPage(self.driver).popup_window()
