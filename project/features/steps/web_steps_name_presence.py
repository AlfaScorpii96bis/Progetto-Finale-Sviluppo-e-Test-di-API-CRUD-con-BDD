# features/steps/web_steps.py
from behave import then

@then('vedo il testo "{text}" nella pagina')
def step_impl(context, text):
    assert text in context.browser.page_source
