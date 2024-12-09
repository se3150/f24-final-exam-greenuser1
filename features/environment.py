from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    context.behave_driver = webdriver.Chrome(options=chrome_options)
    context.behave_driver.implicitly_wait(10)


def after_all(context):
    context.behave_driver.quit()
