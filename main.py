import time
from etherscan import Etherscan
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import utilities as utils

config = utils.read_config()
driver = webdriver.Chrome()
eth = Etherscan(config.get('ether_api_key'))
wallet_address = config.get('wallet_address')


def driver_send_keys_xpath(locator, key):
    """Send keys to element.
    :param locator: Locator of element.
    :param key: Keys to send.
    """
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locator))).send_keys(key)


def driver_click_xpath(locator):
    """Click element.
    :param locator: Locator of element.
    """
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, locator))).click()


def driver_click(locator):
    """Click element.
    :param locator: Locator of element.
    """
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(locator)).click()


def now_gas():
    print('hi')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    now_gas()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
