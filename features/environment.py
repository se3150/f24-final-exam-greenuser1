from selenium import webdriver


def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    context.driver = webdriver.Chrome(options=options)


def after_all(context):
    if context.driver:
        context.driver.quit()
