from behave_webdriver import Chrome 

def before_all(context):
    context.behave_driver = Chrome(headless=True, timeout=10)

def after_all(context):
    if context.behave_driver:
        context.behave_driver.quit()