from selenium import webdriver

def before_all(context):
    """Set up ChromeDriver session before tests."""
    context.driver = webdriver.Chrome(
        executable_path="/usr/local/bin/chromedriver",
        options=webdriver.ChromeOptions().add_argument('--headless')
    )

def after_all(context):
    """Quit ChromeDriver session after tests."""
    if context.driver:
        context.driver.quit()
