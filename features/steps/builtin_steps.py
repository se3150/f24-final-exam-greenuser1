from behave_webdriver.steps import * # ignore
import time 
from behave import given, when ,then 

@given ('I open the url "{url}"')
def step_open_url(context, url):
    context.behave_driver.get(url)

@when ('I enter the message "{message}" to encode')
def step_enter_message_to_encode(context, message):
    message_input = context.behave_driver.find_element_by_id("inputText")
    message_input.clear()
    message_input.send_keys(message)


@when ('I enter the message "{message}" to decode')
def step_enter_message_to_decode(context, message):
    message_input = context.behave_driver.find_element_by_id("inputText")
    message_input.clear()
    message_input.send_keys(message)

@when ('I set the Caesar shift value to "{shift}"')
def step_set_shift_value(context, shift):
    shift_input = context.behave_driver.find_element_by_id("shift")
    shift_input.clear()
    shift_input.send_keys(shift)

@when('i click the encode button')
def step_click_encode_button(context):
    encode_button = context.behave_driver.find_element_by_id("encode")
    encode_button.click()
    time.sleep(0.2)


@when('i click the decode button')
def step_click_decode_button(context):
    decode_button = context.behave_driver.find_element_by_id("decode")
    decode_button.click()
    time.sleep(0.2)

@then('I should see the result"{expected_result}"')
def steo_verify_result(context, expected_result):
    result_element = context.behave_driver.find_element_by_id("outputText")
    actual_result = result_element.text 
    assert actual_result == expected_result, f"Expected '{expected_result}', but got '{actual_result}'"