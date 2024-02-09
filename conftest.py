import pytest
from selenium import webdriver
import os
import configparser

# Load the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

@pytest.fixture()
def driver():
    # Initialize the WebDriver
    username = os.getenv("LT_USERNAME")
    accessKey = os.getenv("LT_ACCESS_KEY")

    gridUrl = config.get('CLOUDGRID', 'grid_url')

    web_driver = webdriver.ChromeOptions()
    platform = config.get('ENV', 'platform')
    browser_name = config.get('ENV', 'browser_name')

    lt_options = {
        "user": username,
        "accessKey": accessKey,
        "build": config.get('CLOUDGRID', 'build_name'),
        "name": config.get('CLOUDGRID', 'test_name'),
        "platformName": platform,
        "w3c": config.getboolean('CLOUDGRID', 'w3c'),
        "browserName": browser_name,
        "browserVersion": config.get('CLOUDGRID', 'browser_version'),
        "selenium_version": config.get('CLOUDGRID', 'selenium_version'),
        "visual": config.get('CLOUDGRID', 'visual')
    }

    options = web_driver
    options.set_capability('LT:Options', lt_options)

    url = f"https://{username}:{accessKey}@{gridUrl}"

    driver = webdriver.Remote(
        command_executor=url,
        options=options
    )

    yield driver

    driver.quit