# features/steps/web_steps.py
@then('vedo il messaggio "{message}"')
def step_impl(context, message):
    assert message in context.browser.page_source
