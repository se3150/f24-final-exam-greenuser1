from selenium import webdriver


def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    context.driver = webdriver.Chrome(options=options)
    context.driver.set_page_load_timeout(10)


def after_all(context):
    if hasattr(context, 'driver') and context.driver:
        context.driver.quit()
