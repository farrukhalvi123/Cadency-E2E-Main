import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import os
import glob
import subprocess
from Constants.URLS import TestData
from Features.Steps.Commons import cadencyweb
from Pages.LoginPage import LoginPage


def before_scenario(context,scenario):
    launch_browser(context,scenario)

def after_scenario(context, scenario):
    context.driver.close()
    context.driver.quit()

def launch_browser(context,scenario):
    if TestData.BROWSER == 'chrome':
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2, 'download.default_directory': os.getcwd() + '\\TestData\\TestExcelsandPDFS\\'}
        # options.add_argument("--headless")
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=800,600")
        options.add_argument("--disable-popup-blocking")
        # options.add_argument("--headless")
        options.add_argument("--ignore-certificate-error")
        options.add_argument("--ignore-ssl-errors")
        options.add_argument("--disable-notifications")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-blink-features=AutomationControlled")
        if TestData.PLATFORM == 'Browser Stack':
            desired_cap = {
                'os_version': '10',
                'resolution': '1920x1080',
                'browser': 'Firefox',
                'browser_version': '90.0',
                'os': 'Windows',
                'name': '1st Parallel test',  # test name
                'build': 'BStack Build Number 1'  # CI/CD job or build name
            }
            context.driver = webdriver.Remote(
                command_executor='https://speedhomebrowser_tiWF2J:s9coaxk36do24scdqy5Q@hub-cloud.browserstack.com/wd/hub',
                desired_capabilities=desired_cap)  # we need to add the account url on which we want to run this test
        elif TestData.PLATFORM == 'local':
            context.driver = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())
        elif TestData.PLATFORM == 'docker':
            remote_url = os.getenv('SELENIUM_GRID_URL')
            # os.environ['DISPLAY'] = ':0'
            time.sleep(5)
            context.driver = webdriver.Remote(command_executor=f'http://172.21.0.3:5555/wd/hub',
                                              desired_capabilities=DesiredCapabilities.CHROME, options=options)
        context.driver.maximize_window()
    elif TestData.BROWSER == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument("--disable-notifications")
        context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif TestData.BROWSER == 'edge':
        context.driver = webdriver.Edge(executable_path=EdgeChromiumDriverManager().install())
        context.driver.maximize_window()
    context.cadency = cadencyweb(context.driver)