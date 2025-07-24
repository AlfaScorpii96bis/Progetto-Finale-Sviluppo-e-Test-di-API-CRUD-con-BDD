# features/steps/web_steps.py
@then('non vedo il testo "{text}" nella pagina')
def step_impl(context, text):
    assert text not in context.browser.page_source
