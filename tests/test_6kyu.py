from task_6kyu import *

def test_abbreviate():
    
    assert abbreviate("internationalization") == "i18n"
    assert abbreviate("accessibility") == "a11y"
    assert abbreviate("Accessibility") == "A11y"
    assert abbreviate("elephant-ride") == "e6t-r2e"