from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from behave import given, when, then


@given('I open the url "{url}"')
def step_open_url(context, url):
    context.driver.get(url)


@when('I enter the message "{message}" to encode')
def step_enter_message_to_encode(context, message):
    message_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "inputText"))
    )
    message_input.clear()
    message_input.send_keys(message)


@when('I enter the message "{message}" to decode')
def step_enter_message_to_decode(context, message):
    message_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "inputText"))
    )
    message_input.clear()
    message_input.send_keys(message)


@when('I set the Caesar shift value to "{shift}"')
def step_set_shift_value(context, shift):
    shift_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "shift"))
    )
    shift_input.clear()
    shift_input.send_keys(shift)


@when('I click the encode button')
def step_click_encode_button(context):
    encode_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "encode"))
    )
    encode_button.click()


@when('I click the decode button')
def step_click_decode_button(context):
    decode_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "decode"))
    )
    decode_button.click()


@then('I should see the result "{expected_result}"')
def step_verify_result(context, expected_result):
    result_element = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "outputText"))
    )
    actual_result = result_element.text
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"
