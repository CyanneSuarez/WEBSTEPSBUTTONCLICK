# features/steps/web_steps.py

from behave import when
from selenium import webdriver

# Initialize the WebDriver
driver = webdriver.Chrome()

@when('I click the "{button_text}" button')
def step_impl(context, button_text):
    button = driver.find_element_by_xpath(f"//button[text()='{button_text}']")
    button.click()
