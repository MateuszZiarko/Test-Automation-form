from test_parleto.Helpers.support_functions import *
from test_parleto.Helpers.DataGenerator import *
from test_parleto.config.test_settings import TestSettings
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        self.driver = driver

    def click_submit_button(self):
        element = wait_for_visibility_of_element_xpath(self.driver, TestSettings.xpath_form_wyslij_button)
        element.click()

    def info_submit_button(self):
        actual_errors = self.driver.find_elements(By.XPATH, TestSettings.xpath_form_actual_errors)
        assert len(actual_errors) == 6, f"Expected to see 6 errors, but got '{len(actual_errors)}'"

    def send_name(self):
        name = DataGenerator().generate_correct_name()
        wait_for_visibility_of_element_xpath(self.driver, TestSettings.xpath_form_osoba)
        element = self.driver.find_element(By.XPATH, TestSettings.xpath_form_osoba)
        element.click()
        element.send_keys(name + " ")
        if name == element.get_attribute("value"):
            assert name == element.get_attribute("value")
            return True
        return False

    def send_last_name(self):
        name = DataGenerator().generate_correct_name()
        wait_for_visibility_of_element_xpath(self.driver, TestSettings.xpath_form_osoba)
        element = self.driver.find_element(By.XPATH, TestSettings.xpath_form_osoba)
        element.click()
        element.send_keys(name)
        if name == element.get_attribute("value"):
            assert name == element.get_attribute("value")
            return True
        return False

    def send_pesel(self):
        pesel = DataGenerator().generate_random_pesel()
        wait_for_visibility_of_element_xpath(self.driver, TestSettings.xpath_form_pesel)
        element = self.driver.find_element(By.XPATH, TestSettings.xpath_form_pesel)
        element.click()
        element.send_keys(pesel)
        assert pesel == element.get_attribute("value")
        if pesel == element.get_attribute("value"):
            return True
        return False

    def send_date(self):
        date = DataGenerator().generate_random_date()
        wait_for_visibility_of_element_xpath(self.driver, TestSettings.xpath_form_data_urodzenia)
        element = self.driver.find_element(By.XPATH, TestSettings.xpath_form_data_urodzenia)
        element.click()
        element.send_keys(date)
        assert date == element.get_attribute("value")
        if date == element.get_attribute("value"):
            return True
        return False

    def send_email(self):
        email = DataGenerator().generate_random_email()
        wait_for_visibility_of_element_xpath(self.driver, TestSettings.xpath_form_email)
        element = self.driver.find_element(By.XPATH, TestSettings.xpath_form_email)
        element.click()
        element.send_keys(email)
        assert email == element.get_attribute("value")
        if email == element.get_attribute("value"):
            return True
        return False

    def send_password(self):
        password = DataGenerator().password()
        wait_for_visibility_of_element_xpath(self.driver, TestSettings.xpath_form_haslo)
        element = self.driver.find_element(By.XPATH, TestSettings.xpath_form_haslo)
        element.click()
        element.send_keys(password)
        assert password == element.get_attribute("value")
        if password == element.get_attribute("value"):
            return True
        return False

    def send_password_confirm(self):
        password = DataGenerator().password()
        wait_for_visibility_of_element_xpath(self.driver, TestSettings.xpath_form_powtorz_haslo)
        element = self.driver.find_element(By.XPATH, TestSettings.xpath_form_powtorz_haslo)
        element.click()
        element.send_keys(password)
        assert password == element.get_attribute("value")
        if password == element.get_attribute("value"):
            return True
        return False

    def popup_window(self):
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        text_from_alert = alert.text
        expected_text = "form submited!"
        assert expected_text == text_from_alert, \
            f'Error. Expected text: {expected_text}, but actual text: {text_from_alert}'
        alert.accept()

    def without_one_data(self):
        actual_errors = self.driver.find_elements(By.XPATH, TestSettings.xpath_form_actual_errors)
        assert len(actual_errors) == 1, f"Expected to see 1 errors, but got '{len(actual_errors)}'"

    def without_two_data(self):
        actual_errors = self.driver.find_elements(By.XPATH, TestSettings.xpath_form_actual_errors)
        assert len(actual_errors) == 2, f"Expected to see 2 errors, but got '{len(actual_errors)}'"

    def send_password_different(self):
        password = DataGenerator().different_password()
        wait_for_visibility_of_element_xpath(self.driver, TestSettings.xpath_form_powtorz_haslo)
        element = self.driver.find_element(By.XPATH, TestSettings.xpath_form_powtorz_haslo)
        element.click()
        element.send_keys(password)
        assert password == element.get_attribute("value")
        if password == element.get_attribute("value"):
            return True
        return False
