from selenium import webdriver

def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    context.driver = webdriver.Chrome(options=options)

def after_all(context):
    context.driver.quit()
