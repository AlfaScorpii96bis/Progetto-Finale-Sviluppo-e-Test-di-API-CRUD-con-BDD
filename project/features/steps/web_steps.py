# features/steps/web_steps.py
from behave import when

@when('clicco sul pulsante {button}')
def step_impl(context, button):
    context.browser.find_element_by_id(button).click()
