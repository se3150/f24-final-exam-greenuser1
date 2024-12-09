from selenium import webdriver

def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--remote-debugging-port=9222")
    context.driver = webdriver.Chrome(options=options)

def after_all(context):
    context.driver.quit()
