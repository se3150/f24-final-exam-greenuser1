from selenium import webdriver


def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    context.behave_driver = webdriver.Chrome(options=options)


def after_all(context):
    if hasattr(context, 'behave_driver'):
        context.behave_driver.quit()
