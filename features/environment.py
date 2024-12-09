from selenium import webdriver
import os 



def before_all(context):
    chromedriver_path = '/Users/marcoraromoreno/Desktop/chromedriver-mac-x64/chromedriver'
    if not os.path.exists(chromedriver_path):
        raise FileNotFoundError(f"Chromedriver not found at {chromedriver_path}")
    options = webdriver.ChromeOptions()
    options.headless = True
    context.behave_driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)

def after_all(context):
    if hasattr(context, 'behave_driver') and context.behave_driver:
        context.behave_driver.quit()
