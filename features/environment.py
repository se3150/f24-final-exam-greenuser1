from selenium import webdriver

def before_all(context):
    options = webdriver.ChromeOptions()
    options.headless = True
    context.behave_driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)

def after_all(context):
    if context.behave_driver:
        context.behave_driver.quit()
