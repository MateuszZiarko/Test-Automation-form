from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains


def hover_over_element(driver, xpath):
    element = driver.find_element_by_xpath(xpath)
    hover = ActionChains(driver).move_to_element(element)
    hover.perform()


def wait_for_visibility_of_element_xpath(driver, xpath, time_to_wait=10):
    try:
        element = WebDriverWait(driver, time_to_wait).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        element = False
    return element


def wait_for_visibility_of_element_id(driver, element_id, time_to_wait=10):
    try:
        element = WebDriverWait(driver, time_to_wait).until(EC.visibility_of_element_located((By.ID, element_id)))
    except TimeoutException:
        element = False
    return element


def wait_for_invisibility_of_element_xpath(driver, xpath, time_to_wait=10):
    element = WebDriverWait(driver, time_to_wait).until(EC.invisibility_of_element_located((By.XPATH, xpath)))
    return element


def wait_for_invisibility_of_element_id(driver, element_id, time_to_wait=10):
    element = WebDriverWait(driver, time_to_wait).until(EC.invisibility_of_element_located((By.ID, element_id)))
    return element
